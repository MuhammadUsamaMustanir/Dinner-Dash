from django.shortcuts import render

from .models import User


def get_all_users(request, first_name):
    user = User.objects.all()
    context = {"user": user}
    render(request, 'user/templates/users.html', context)
