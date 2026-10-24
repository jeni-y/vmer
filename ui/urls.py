from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('login_verify/',views.login_verify,name='login_verify'),
    #path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    #LOGIN_URL = '/login/'
    #LOGIN_REDIRECT_URL = '/index/'
    #LOGOUT_REDIRECT_URL = '/'
 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_user/',views.register_user,name='register_user'),
    path('index/',views.index, name='index'),
    path('vm/',views.vm,name='vm'),
    path('later/',views.later,name='later'),
]