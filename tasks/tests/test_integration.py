from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task


class TaskIntegrationTest(APITestCase):
    def test_task_lifecycle(self):
        """
        Test creating, retrieving, updating, and deleting a task.
        """

        # Step 1: Create a new task
        create_payload = {"title": "Integration Task", "completed": False}
        create_response = self.client.post('/api/tasks/', create_payload)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(create_response.data['title'], "Integration Task")
        self.assertFalse(create_response.data['completed'])

        # Extract the created task's ID
        task_id = create_response.data['id']

        # Step 2: Retrieve the task
        retrieve_response = self.client.get(f'/api/tasks/{task_id}/')
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['title'], "Integration Task")
        self.assertFalse(retrieve_response.data['completed'])

        # Step 3: Update the task
        update_payload = {"title": "Updated Integration Task", "completed": True}
        update_response = self.client.put(f'/api/tasks/update/{task_id}/', update_payload)
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['title'], "Updated Integration Task")
        self.assertTrue(update_response.data['completed'])

        # Step 4: Delete the task
        delete_response = self.client.delete(f'/api/tasks/{task_id}/delete/')
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # Step 5: Verify the task no longer exists
        verify_response = self.client.get(f'/api/tasks/{task_id}/')
        self.assertEqual(verify_response.status_code, status.HTTP_404_NOT_FOUND)

