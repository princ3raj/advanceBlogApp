from django.urls import path
from django.contrib.auth import views as auth_views

from discord import views


urlpatterns = [

    path('accounts/login/', auth_views.LoginView.as_view(), name="user-login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="user-logout"),
    path('register/', views.register, name="register-user"),
    path('', views.index, name="index")

]
