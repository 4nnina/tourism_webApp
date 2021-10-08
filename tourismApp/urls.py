from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('logIn', views.logIn, name="logIn"),
    path('logOut', views.logOut, name="logOut"),
    path('edit', views.edit, name="edit"),
    path('edit/<str:pk>', views.editArt, name="editArt"),
    path('<str:pk>', views.item, name='item')

    #path('example/homepage', views.homepage, name="homepage"),
    #path('example/', views.example, name='example'),
]