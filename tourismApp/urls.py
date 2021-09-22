from django.urls import path

from .import views

urlpatterns = [
    path('', views.logIn, name="logIn"),
    path('homepage/', views.homepage, name="homepage"),
]