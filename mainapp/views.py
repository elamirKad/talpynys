from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Comment, Executor
from django.db.models import Max


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
        try:
            dictionary['comments'] = Comment.objects.filter(task_id=id)
        except:
            dictionary['comments'] = None
        if request.method == "POST":
            if 'send_comment' in request.POST:
                username = request.user.username
                comment = Comment(task_id=id, username=username, comment=request.POST.get('comment'))
                comment.save()
            elif 'accept' in request.POST:
                username = request.user
                if not Executor.objects.filter(username=username).exists():
                    executor = Executor(username=username, task=task)
                    executor.save()
                    task.completed = True
                    task.save()
            return redirect(f'/app/tasks/{id}')
        return render(request, 'task.html', dictionary)
    else:
        data = Task.objects.all()
        dictionary = {
            'tasks': data
        }
        return render(request, 'tasks.html', dictionary)

def create_task(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            username = request.user.username
            title = request.POST.get('title')
            description = request.POST.get('description')
            reward = request.POST.get('reward')
            t = Task(title=title, description=description, reward=reward, username=username)
            t.save()
            return redirect(f'/app/tasks/{t.id}')
        return redirect('/app/create/')
    else:
        return render(request, 'create.html')

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
        if keywords:
            data = Task.objects.filter(title__icontains=keywords)
        else:
            data = Task.objects.all()
        max_reward = data.aggregate(Max('reward'))
        if 'minreward' in request.GET:
            data = data.exclude(reward__lte=request.GET.get('minreward'))
        if 'maxreward' in request.GET:
            data = data.exclude(reward__gt=request.GET.get('maxreward'))
        if 'hidecompleted' in request.GET:
            data = data.exclude(completed=True)
        dictionary = {
            'keywords': keywords,
            'tasks': data,
            'max_reward': max_reward['reward__max']
        }
        return render(request, 'search.html', dictionary)
    else:
        max_reward = Task.objects.aggregate(Max('reward'))
        dictionary = {
            'max_reward': max_reward['reward__max'],
            'keywords': ''
        }
        return render(request, 'search.html', dictionary)