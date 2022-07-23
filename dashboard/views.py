from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ProfilePic


# Create your views here.
def dashboard(request, username):
    account = User.objects.get(username=username)
    dictionary = {
        'username': account.username,
        'first_name': account.first_name,
        'last_name': account.last_name
    }
    try:
        pfp = ProfilePic.objects.get(username=username)
        dictionary['pfp'] = pfp
    except:
        dictionary['pfp'] = None

    return render(request, 'dashboard.html', dictionary)

def settings(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return redirect('/app/tasks/')
    account = User.objects.get(username=username)
    dictionary = {
        'username': account.username,
        'first_name': account.first_name,
        'last_name': account.last_name
    }
    if request.method == "POST":
        if ProfilePic.objects.filter(username=username).exists():
            profpic = ProfilePic.objects.get(username=username)
            if profpic.image:
                profpic.image.delete()
            ProfilePic.objects.filter(username=username).delete()
        pfp = request.FILES.get('pfp')
        profilepic = ProfilePic()
        profilepic.username = username
        profilepic.image = pfp
        profilepic.save()
        return render(request, 'settings.html', dictionary)
    else:
        return render(request, 'settings.html', dictionary)