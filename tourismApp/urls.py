from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Art', views.filterItemArt, name="filterItemArt"),
    path('Tour', views.filterItemTour, name="filterItemTour"),
    path('register', views.register, name="register"),
    path('logIn', views.logIn, name="logIn"),
    path('logOut', views.logOut, name="logOut"),
    path('editArt', views.editArt, name="editArt"),
    path('editTour',views.editTour, name="editTour"),
    path('edit/newArt', views.newArt, name="newArt"),
    path('edit/newTour', views.newTour, name="newTour"),
    path('edit/<str:classid>', views.editPoI1, name="editPoI1"),
    path('edit/translation/<str:classid_lang>', views.editPoI2, name="editPoI2"),
    path('edit/tour/<str:classid_lang>', views.editOneTour, name="editOneTour"),
    path('edit/tour/<str:classid>/points', views.editTourPoi, name="editTourPoi"),
    path('Art/<str:classid_lang>', views.itemPoI, name='itemPoI'),
    path('Tour/<str:classid_lang>', views.itemTour, name='itemTour'),

    #path('example/homepage', views.homepage, name="homepage"),
    #path('example/', views.example, name='example'),
]