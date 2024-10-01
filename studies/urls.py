from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('add/', views.add_study, name='add_study'),
    path('edit/<int:study_id>/', views.edit_study, name='edit_study'),
    path('view/<int:study_id>/', views.view_study, name='view_study'),
    path('delete/<int:study_id>/', views.delete_study, name='delete_study'),
]
