from django.shortcuts import render
from todo.models import Task


def home(request):
    # filter se lay multidata con get se lay 1 data
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_complete=True)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }

    return render(request, 'home.html', context)
