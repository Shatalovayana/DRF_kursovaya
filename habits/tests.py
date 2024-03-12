from django.urls import reverse

from habits.models import Habit
from users.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.user.set_password('test')
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place='дом',
            time='10:00:00',
            action='делать зарядку',
            period=1,
            reward='кофе',
            time_to_complete='2',
            is_published=True,
            )

    def test_get_habit_create(self):
        """Тестирование создания привычки."""
        data = {
            'user': self.user,
            'place': 'дом',
            'time': '12:00:00',
            'action': 'делать растяжку',
            'period': 1,
            'reward': 'сон',
            'time_to_complete': 2
        }

        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_get_habit_list(self):
        """Тестирование получения списка привычек."""
        response = self.client.get(
            reverse('habits:habit-list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_habit_retrieve(self):
        response = self.client.get(
            reverse('habits:habits-get', kwargs={'pk': self.habit.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_habit_update(self):
        """Тестирование редактирования привычки."""
        data = {
            'time': '11:00:00',
            'action': 'делать растяжку',
            'reward': 'сок',
            'period': 2,
            'time_to_complete': 1,
        }

        response = self.client.patch(
            reverse('habits:habits-update', kwargs={'pk': self.habit.pk}),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_habit_delete(self):
        """Тестирование удаления привычки."""
        response = self.client.delete(
            reverse('habits:habits-delete', kwargs={'pk': self.habit.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
