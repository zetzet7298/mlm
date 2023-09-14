from django.urls import path
from . import views

urlpatterns = [
    path('multi-level/', views.index, name='multi_level.index'),
    path('create-user', views.store_user, name='multi_level.store'),
    path('multi-level/data/delete-all', views.delete_all, name='multi_level.delete_all'),
    path('multi-level/<int:id>', views.detail_as_json, name='multi_level.detail_as_json'),
]