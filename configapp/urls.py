from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('viloyatlar/', views.viloyat_list, name='viloyat-list'),
    path('viloyat/<int:viloyat_id>/tumanlar/', views.tuman_list, name='tuman-list'),
    path('tuman/<int:tuman_id>/mahallalar/', views.mahalla_list, name='mahalla-list'),
]