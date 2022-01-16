from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

path('home/',views.home,name='home'),
path('edit_members/',views.edit_members,name='edit_members'),
path('delete_members/',views.delete_members,name='delete_members'),
path('tour/',views.tour,name='tour'),
path('tourmanagement/',views.tourmanagement,name='tourmanagement'),
path('touredit/<int:pk>',views.touredit,name='edittour'),
path('edittoursubmit/',views.edittoursubmit,name='edittoursubmit'),
path('delete_tour/',views.delete_tour,name='delete_tour'),
path('upload_files/<int:pk>/',views.upload_files,name='upload_files')

]