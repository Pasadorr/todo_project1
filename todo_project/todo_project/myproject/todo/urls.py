from django.urls import path
from .views import task_list, toggle_task, delete_task, edit_task, add_task

urlpatterns = [
    path('', task_list, name='task_list'),  # Список задач
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),  # Редактирование задачи
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('toggle_task/<int:task_id>/', toggle_task, name='toggle_task'),
    path('add_task/', add_task, name='add_task'),# Новый путь для переключения задачи
]