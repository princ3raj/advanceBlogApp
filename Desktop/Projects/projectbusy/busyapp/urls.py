from django.urls import path, include


from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('api/<int:phone_number>/<str:text_message>',views.api,name="api"),
    path('fetch',views.fetchdata,name="fetchdata")

    
]