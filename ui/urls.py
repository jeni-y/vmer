from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='index'),
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),


]
