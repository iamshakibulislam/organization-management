from django.urls import path
from . import views

urlpatterns=[
    
    path('main_page/',views.main_page,name='main_procurement_page'),
    path('add_procurements_for_goods/',views.add_procurements_for_goods,name='add_procurements_for_goods'),
    path('procurement_details/<int:pk>/',views.procurement_details,name='procurement_details'),
    path('update_procurements_for_goods/<int:pk>/',views.update_procurements_for_goods,name='update_procurements_for_goods'),
    path('delete_procurements_for_goods/',views.delete_procurements_for_goods,name='delete_procurements_for_goods'),

]