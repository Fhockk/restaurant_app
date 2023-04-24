from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from employees.models import Employee


class EmployeeViewTestCase(APITestCase):
    url = '/api/v1/employees/'

    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'username': 'testuser',
            'first_name': 'testfirst_name',
            'last_name': 'testlast_name',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        self.invalid_payload = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        self.update_payload = {
            'username': 'updateduser',
            'first_name': 'updatedfirst_name',
            'last_name': 'updatedlast_name',
            'email': 'updateduser@example.com',
            'password': 'updatedpassword',
        }

    def test_create_valid_user(self):
        response = self.client.post(self.url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().username, 'testuser')
        self.assertEqual(Employee.objects.get().email, 'testuser@example.com')

    def test_create_invalid_user(self):
        response = self.client.post(self.url, self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_user(self):
        employee = Employee.objects.create(
            username='testuser2',
            first_name='testfirst_name2',
            last_name='testlast_name2',
            email='testuser2@example.com',
            password='testpassword2'
        )
        response = self.client.put(f'{self.url}{employee.id}/', self.update_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        employee.refresh_from_db()
        self.assertEqual(employee.username, 'updateduser')
        self.assertEqual(employee.first_name, 'updatedfirst_name')
        self.assertEqual(employee.last_name, 'updatedlast_name')
        self.assertEqual(employee.email, 'updateduser@example.com')

    def test_delete_valid_user(self):
        employee = Employee.objects.create(
            username='testuser3',
            first_name='testfirst_name3',
            last_name='testlast_name3',
            email='testuser3@example.com',
            password='testpassword3'
        )
        response = self.client.delete(f'{self.url}{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
