from django.urls import path

from .views import get_teachers

urlpatterns = [
    path("", get_teachers, name="teachers"),
]
