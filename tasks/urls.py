from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index),
    path('deleteTask/<int:task_id>/', views.delete_task)
]
