from habits.apps import HabitsConfig
from django.urls import path

from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('habits/public/', HabitPublicListAPIView.as_view(), name='habit-public'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits-get'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits-delete'),
]
