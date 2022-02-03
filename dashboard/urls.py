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
path('upload_files/<int:pk>/',views.upload_files,name='upload_files'),
path('show_files/<int:pk>/',views.show_files,name='show_files'),
path('add_tour_place/',views.add_tour_place,name='add_tour_place'),
path('add_sub_sector/',views.add_sub_sector,name='add_sub_sector'),
path('logs/<int:pk>/',views.get_logs,name='logs')

]