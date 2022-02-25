from django.urls import path
from . import views

urlpatterns = [
    path('add_training/', views.add_training, name='add_training'),
    path('training_list/', views.training_list, name='training_list'),
    path('training_edit/<int:pk>/', views.training_edit, name='training_edit'),
    path('add_training_category/', views.add_training_category, name='add_training_category'),
    path('training_details/<int:pk>/', views.training_details, name='training_details'),
    path('training_delete/', views.training_delete, name='training_delete'),
]
