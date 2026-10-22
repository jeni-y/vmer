from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('login_verify/',views.login_verify,name='login_verify'),
    path('home/',views.home,name='home'),

    path('register_user/',views.register_user,name='register_user'),
]