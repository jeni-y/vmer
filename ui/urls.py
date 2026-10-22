from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/register/',views.register,name='register'),


]
