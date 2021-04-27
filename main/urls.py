from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:id>/', views.deletePlan, name="deletePlan"),
    path('', views.home, name="home"),
    
]
