from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Art', views.filterItemArt, name="filterItemArt"),
    path('Tour', views.filterItemTour, name="filterItemTour"),
    path('register', views.register, name="register"),
    path('logIn', views.logIn, name="logIn"),
    path('logOut', views.logOut, name="logOut"),
    path('edit', views.edit, name="edit"),
    path('edit/newArt', views.newArt, name="newtArt"),
    path('edit/<str:classid_lang>', views.editArt, name="editArt"),
    path('<str:classid_lang>', views.item, name='item'),

    #path('example/homepage', views.homepage, name="homepage"),
    #path('example/', views.example, name='example'),
]