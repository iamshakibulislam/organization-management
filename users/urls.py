from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

path('signup/',views.signup,name='signup'),
path('login/',views.login,name='login'),
path('add_member/',views.addMember,name='add_member'),
path('logout/',views.logout,name='logout'),
path('profile/',views.profile,name='profile'),

]