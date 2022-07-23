from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import CreateNewTask


# Create your views here.
def tasks(request, id=None):
    if id:
        task = Task.objects.get(id=id)
        dictionary = {
            'title': task.title,
            'description': task.description,
            'created_date': task.created_date,
            'reward': task.reward,
            'completed': task.completed,
            'username': task.username
        }
        return render(request, 'task.html', dictionary)
    else:
        data = Task.objects.all()
        dictionary = {
            'tasks': data
        }
        return render(request, 'tasks.html', dictionary)

def create_task(request):
    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            reward = form.cleaned_data["reward"]
            if request.user.is_authenticated:
                username = request.user.username
            t = Task(title=title, description=description, reward=reward, username=username)
            t.save()
        return redirect(f'/app/tasks/{t.id}')
    else:
        form = CreateNewTask()
        return render(request, 'create.html', {'form':form})