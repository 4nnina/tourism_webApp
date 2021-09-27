from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('logIn', views.logIn, name="logIn"),
    path('logOut', views.logOut, name="logOut"),
    path('example/homepage', views.homepage, name="homepage"),
    path('example/', views.example, name='example'),
]