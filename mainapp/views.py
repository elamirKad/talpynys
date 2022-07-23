from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import CreateNewTask


# Create your views here.
def tasks(request, id=None):
    if id:
        task = Task.objects.get(id=id)
        dictionary = {
            'id': task.id,
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

def update(request, id=None):
    if id:
        task = Task.objects.get(id=id)
        if request.method == "POST":
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.reward = request.POST.get('reward')
            if request.POST.get('completed') == "on":
                task.completed = True
            elif request.POST.get('completed') == None:
                task.completed = False
            task.save()
            return redirect(f"/app/tasks/{id}")
        else:
            dictionary = {
                'username': task.username,
                'title': task.title,
                'description': task.description,
                'reward': task.reward,
                'completed': task.completed,
            }
            return render(request, 'update.html', dictionary)

def search(request):
    if request.method == "GET":
        keywords = request.GET.get('keywords')
        data = Task.objects.filter(title__icontains=keywords)
        dictionary = {
            'tasks': data
        }
        return render(request, 'search.html', dictionary)
    else:
        dictionary = {

        }
        return render(request, 'search.html', dictionary)