import os
import requests

from config.settings import TG_API_KEY
from habits.models import Habit


def send_message_to_tg(habit_id):
    habit = Habit.objects.get(id=habit_id)
    url_post = 'https://api.telegram.org/bot'.format(TG_API_KEY, 'sendMessage')
    chat_id = habit.user.tg_id

    message = (f'Место: {habit.place}\n'
               f'Время начала: {habit.time}\n'
               f'Действие: {habit.action}\n'
               f'Награда: {habit.reward or habit.connected_habit}\n'
               f'Время на выполнение: {habit.time_to_complete}\n')

    try:
        requests.post(url_post, json={'chat_id': chat_id, 'text': message})
    except Exception as e:
        print(f'Ошибка при отправке сообщения: {e}')
    print('Отправка сообщений закончена.')
