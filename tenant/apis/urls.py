from .views import home, update
from django.urls import path

urlpatterns = [
    path('',home.home_view.as_view()),
    path('update/',update.update_view.as_view()),
]