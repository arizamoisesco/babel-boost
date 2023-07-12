from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #Login previo
    #path('login/', views.user_login, name='login'),
    #Login / logout urls
    #path('login', auth_views.LoginView.as_view(), name='login'),
    #path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]