from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator, TimeToCompleteValidator, PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(connected_habit='connected_habit',
                                     reward='reward',
                                     sign_of_a_pleasant_habit='sign_of_a_pleasant_habit'),
                      TimeToCompleteValidator(time_to_complete='time_to_complete'),
                      PeriodValidator(period='period')]
