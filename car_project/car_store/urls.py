from django.urls import path, include
from .views import *


urlpatterns = [
    path('', cars_list, name='cars_list'),
    path('<int:pk>', cars_detail, name='cars_detail'),
    path('create', cars_create, name='cars_create'),
    path('<int:pk>/update', cars_update, name='cars_update'),
    path('<int:pk>/delete', cars_delete, name='cars_delete'),
]
