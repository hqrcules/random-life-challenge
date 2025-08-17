from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_challenge_view, name='daily_challenge'),
    path('progress/', views.progress_view, name='progress'),
    path('history/', views.history_view, name='history'),
    path('api/progress-data/', views.progress_data_api, name='progress_data_api'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
