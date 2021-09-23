from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logIn', views.logIn, name="logIn"),
    path('example/homepage', views.homepage, name="homepage"),
    path('example/', views.example, name='example'),
]