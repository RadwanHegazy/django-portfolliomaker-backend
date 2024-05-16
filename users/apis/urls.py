from .views import login, register, profile
from django.urls import path

urlpatterns = [
    path('auth/login/',login.login_view.as_view()),
    path('auth/register/',register.register_view.as_view()),
    path('profile/',profile.profile_view.as_view()),
]