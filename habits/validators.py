import datetime

from rest_framework.exceptions import ValidationError

from habits.models import Habit


class HabitValidator:
    """Валидатор привычки"""

    def __init__(self, connected_habit, reward, sign_of_a_pleasant_habit):
        self.sign_of_a_pleasant_habit = sign_of_a_pleasant_habit
        self.connected_habit = connected_habit
        self.reward = reward

    def __call__(self, value):
        sign_of_a_pleasant_habit = value.get(self.sign_of_a_pleasant_habit)
        reward = value.get(self.reward)
        connected_habit = value.get(self.connected_habit)

        if sign_of_a_pleasant_habit and (reward or connected_habit):
            raise ValidationError(
                'У приятной привычки не может быть вознаграждения'
                ' или связанной привычки!'
            )

        if sign_of_a_pleasant_habit:
            return True

        if reward and connected_habit:
            raise ValidationError(
                'Нельзя одновременно выбрать приятную привычку '
                'и вознаграждение!'
            )

        if not reward and not connected_habit:
            raise ValidationError(
                'Необходимо указать приятную привычку '
                'или вознаграждение!'
            )

        if not reward:
            try:
                habit = Habit.objects.get(pk=connected_habit.pk)
                if not habit.sign_of_a_pleasant_habit:
                    raise ValidationError('Привычка не является приятной!')
            except Habit.DoesNotExist:
                raise ValidationError('Привычка не найдена!')


class TimeToCompleteValidator:
    """Валидатор времени выполнения"""

    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value):
        time = value.get(self.time_to_complete)

        if time > 2:
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд!'
                )


class PeriodValidator:
    """Валидатор периодичности"""
    def __init__(self, period):
        self.period = period

    def __call__(self, value):
        period = value.get(self.period)

        if period <= 1 or period >= 7:
            raise ValidationError(
                'Периодичность должна быть в диапазоне от 1 до 7 (дни)'
            )
