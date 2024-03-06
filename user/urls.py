from django.urls import path

from . import views

urlpatterns = [
    path("<str:first_name>", views.get_all_users),
    path("", views.user_index),
]
