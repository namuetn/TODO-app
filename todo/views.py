from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task


def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = True
    task.save()

    return redirect('home')