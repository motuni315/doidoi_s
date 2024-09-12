from django.urls import path
from doidoi_s import views

urlpatterns = [
    path('', views.index, name='index'),
]