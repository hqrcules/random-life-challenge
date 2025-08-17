from django.contrib import admin
from .models import Category, Challenge, UserChallenge

admin.site.register(Category)
admin.site.register(Challenge)
admin.site.register(UserChallenge)

