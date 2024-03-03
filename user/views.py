from django.shortcuts import render

from .models import User


def get_all_users(request, first_name):
    user = User.objects.filter(first_name=first_name)
    context = {"user": user}
    return render(request, 'users.html', context)
