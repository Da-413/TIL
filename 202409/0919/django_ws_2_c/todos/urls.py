
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_todo/', views.create_todo),
    path('<str:work>/', views.detail_view),
]
