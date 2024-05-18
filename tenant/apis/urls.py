from .views import home, update, get
from django.urls import path

urlpatterns = [
    path('',home.home_view.as_view()),
    path('update/',update.update_view.as_view()),
    path('get/tenant/<str:tenant_name>/',get.tenant_view.as_view()),
    path('get/all/',get.get_all_tenants.as_view()),
]