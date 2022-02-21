from django.urls import path
from . import views

urlpatterns=[
    
    path('main_page/',views.main_page,name='main_procurement_page'),
    path('add_procurements_for_goods/',views.add_procurements_for_goods,name='add_procurements_for_goods'),
    path('procurement_details/<int:pk>/',views.procurement_details,name='procurement_details'),
    path('update_procurements_for_goods/<int:pk>/',views.update_procurements_for_goods,name='update_procurements_for_goods'),
    path('delete_procurements_for_goods/',views.delete_procurements_for_goods,name='delete_procurements_for_goods'),

    path('summery_for_goods/',views.summery_for_goods,name='summery_for_goods'),
    path('add_procurements_for_services/',views.add_procurements_for_services,name='add_procurements_for_services'),
    path('procurement_list_for_services/',views.procurement_list_for_services,name='procurement_list_for_services'),
    path('update_procurements_for_services/<int:pk>/',views.update_procurements_for_services,name='update_procurements_for_services'),
    path('procurement_details_for_services/<int:pk>/',views.procurement_details_for_services,name='procurement_details_for_services'),
    path('delete_procurements_for_service/',views.delete_procurements_for_service,name='delete_procurements_for_service'),
    path('summery_for_services/',views.summery_for_services,name='summery_for_services'),


    path('add_procurements_for_work/',views.add_procurements_for_work,name='add_procurements_for_work'),
    path('procurement_list_for_work/',views.procurement_list_for_work,name='procurement_list_for_work'),
    path('update_procurements_for_work/<int:pk>/',views.update_procurements_for_work,name='update_procurements_for_work'),
    path('procurement_details_for_work/<int:pk>/',views.procurement_details_for_work,name='procurement_details_for_work'),
    path('delete_procurements_for_work/',views.delete_procurements_for_work,name='delete_procurements_for_work'),
     path('summery_for_work/',views.summery_for_work,name='summery_for_work'),
]