from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskDetailAPIView,
    TaskTitlesAPIView
)

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),  # List and Create Tasks
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),  # Retrieve, Update, Delete Task
    path('tasks/titles/', TaskTitlesAPIView.as_view(), name='task-titles'),  # Get Titles of Tasks
]
