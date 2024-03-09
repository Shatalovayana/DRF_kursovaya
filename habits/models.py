from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField(max_length=100, verbose_name='место', **NULLABLE)
    time = models.DateTimeField(verbose_name='время')
    action = models.CharField(max_length=200, verbose_name='действие')
    sign_of_a_pleasant_habit = models.BooleanField(verbose_name='признак приятной привычки', **NULLABLE)
    connected_habit = models.ForeignKey('self', verbose_name='связанная привычка', on_delete=models.CASCADE, **NULLABLE)
    period = models.IntegerField(verbose_name='периодичность')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='время на выполнение')
    is_published = models.BooleanField(verbose_name='признак публичности', default=False)
