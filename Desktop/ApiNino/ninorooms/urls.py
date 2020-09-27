from django.urls import path,include

from . import views




urlpatterns = [


    path('',include('django.contrib.auth.urls')),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('',views.PgRegistration,name='index'),
    path('success',views.success,name="success")

 
    
]
