from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.index, name='client.index'),
    path('client-type', views.client_type_index, name='client_type.index'),
    path('create-client-type', views.store_client_type, name='client_type.store'),
    path('delete-client-type/<id>', views.delete_client_type, name='client_type.delete'),
    path('update-client-type/<id>', views.update_client_type, name='client_type.update'),
]