from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Поменяйте на нужный вам URL
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/edit_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Выбор из базы данных

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'success': True})

    return HttpResponseNotFound()

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/task_list.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Создание формы с данными POST
        if form.is_valid():  # Проверка, валидна ли форма
            form.save()  # Сохранение новой задачи в базе данных
            return redirect('task_list')  # Переход на страницу со списком задач
    else:
        form = TaskForm()  # Пустая форма для отображения

    context = {
        'form': form
    }
    return render(request, 'todo/add_task.html', context)

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'PUT':
        task.completed = not task.completed  # Переключаем состояние
        task.save()
        return JsonResponse({'id': task.id, 'completed': task.completed})  # Возвращаем также новое состояние задачи

    return HttpResponseNotFound()