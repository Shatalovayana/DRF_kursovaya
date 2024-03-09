from datetime import datetime, timedelta

from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from habits.models import Habit
from habits.services import send_message_to_tg


@shared_task
def task_send_msg_to_tg(habit_id):
    send_message_to_tg(habit_id)


for habit in Habit.objects.all():
    habit_time = datetime.combine(datetime.today(), habit.time)
    previous_tasks = PeriodicTask.objects.filter(
        name__contains=f'ID задачи {habit.id}'
    )
    previous_tasks.delete()

    if datetime.now() < habit_time:
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=habit.period,
            period=IntervalSchedule.DAYS,
        )

        PeriodicTask.objects.create(
            interval=schedule,
            name=f'ID задачи {habit.id}. Задача: {habit.action}',
            task='habits.tasks.task_send_msg_to_tg',
            args=[habit.id],
            start_time=habit_time - timedelta(seconds=15)
        )