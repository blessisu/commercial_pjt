from django.urls import path
from . import views


app_name='rents'

urlpatterns = [
    path('', views.rent_list, name=""),
    path('write/', views.rent_write, name="write"),
    path('content/<int:rent_id>/delete/', views.rent_delete, name="delete"),
    path('content/<int:rent_id>/edit', views.rent_edit, name="edit"),
    path('content/<int:rent_id>/', views.rent_content, name="content"),
]
