from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def tasks(request, id=None):
    if id:
        task = Task.objects.get(id=id)
        dictionary = {
            'title': task.title,
            'description': task.description,
            'created_date': task.created_date,
            'reward': task.reward,
            'completed': task.completed
        }
        return render(request, 'task.html', dictionary)
    else:
        data = Task.objects.all()
        dictionary = {
            'tasks': data
        }
        return render(request, 'tasks.html', dictionary)