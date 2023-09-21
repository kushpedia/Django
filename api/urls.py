from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getAllProjects),
    path('projects/<str:pk>/', views.getProject),
]