from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        # Create a sample task for testing
        Task.objects.create(title="Test Task", completed=False)

    def test_get_all_tasks(self):
        """Test retrieving all tasks"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One task created in setUp

    def test_create_task(self):
        """Test creating a new task"""
        payload = {"title": "New Task", "completed": False}
        response = self.client.post('/api/tasks/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Task")

    def test_get_single_task(self):
        """Test retrieving a single task"""
        task = Task.objects.first()  # Retrieve the first task
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Task")
