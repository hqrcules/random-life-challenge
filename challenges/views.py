from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Challenge, UserChallenge, Category
import random
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('daily_challenge')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('daily_challenge')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


@login_required
def daily_challenge_view(request):
    today = timezone.now().date()
    user_challenge = UserChallenge.objects.filter(user=request.user, assigned_date=today).first()

    if not user_challenge:
        all_challenges = list(Challenge.objects.all())
        if all_challenges:
            random_challenge = random.choice(all_challenges)
            user_challenge = UserChallenge.objects.create(
                user=request.user,
                challenge=random_challenge,
                assigned_date=today
            )

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['COMPLETED', 'FAILED']:
            user_challenge.status = status
            if status == 'COMPLETED':
                user_challenge.completed_date = today
            user_challenge.save()
            return redirect('progress')

    return render(request, 'challenges/daily_challenge.html', {'user_challenge': user_challenge})


@login_required
def progress_view(request):
    return render(request, 'challenges/progress.html')


@login_required
def history_view(request):
    challenge_list = UserChallenge.objects.filter(user=request.user).exclude(status='PENDING').order_by(
        '-assigned_date')
    paginator = Paginator(challenge_list, 10)  # Show 10 challenges per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'challenges/history.html', {'page_obj': page_obj})


@login_required
def progress_data_api(request):
    category_data = UserChallenge.objects.filter(
        user=request.user, status='COMPLETED'
    ).values('challenge__category__name').annotate(count=Count('id')).order_by('challenge__category__name')

    category_labels = [item['challenge__category__name'] for item in category_data]
    category_counts = [item['count'] for item in category_data]

    daily_data = UserChallenge.objects.filter(
        user=request.user, status='COMPLETED'
    ).annotate(day=TruncDay('completed_date')).values('day').annotate(count=Count('id')).order_by('day')

    daily_labels = [item['day'].strftime('%Y-%m-%d') for item in daily_data]
    daily_counts = [item['count'] for item in daily_data]

    data = {
        'category_chart': {
            'labels': category_labels,
            'data': category_counts,
        },
        'daily_chart': {
            'labels': daily_labels,
            'data': daily_counts,
        }
    }
    return JsonResponse(data)

