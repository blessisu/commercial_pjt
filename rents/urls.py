from django.urls import path
from . import views


app_name='rents'

urlpatterns = [
    path('', views.rent_list, name=""),
    path('write/', views.rent_write, name="write"),
    path('content/<int:rent_id>/remove/', views.rent_remove, name="remove"),
    path('content/<int:rent_id>/edit', views.rent_edit, name="edit"),
    path('content/<int:rent_id>/', views.rent_content, name="content"),
]
