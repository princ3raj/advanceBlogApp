from django.urls import  path
from . import  views


app_name='iquensans'

urlpatterns=[

    path("signup",views.signup,name="signup"),
    path("login",views.login_view,name="login"),
    path("index",views.index, name="index"),
    path("posts",views.fetchPosts,name="posts"),
    path('like/', views.image_like, name='like'),



]