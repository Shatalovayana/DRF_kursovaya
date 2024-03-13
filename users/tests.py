from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


class UserAPITestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'email': 'test@user.com',
            'password': 'test',
            'tg_id': '1234'
        }

    def test_get_user_register(self) -> None:
        """Тестирование регистрации нового пользователя."""
        data = {
            'email': 'test@user.com',
            'password': 'test',
            'tg_id': '1234'
        }
        response = self.client.post(
            '/users/users/',
            data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
