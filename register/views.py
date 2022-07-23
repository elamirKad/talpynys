from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dashboard.models import AccountExperience

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            experience = AccountExperience(username=user, experience=0)
            experience.save()
        return redirect('/app/tasks/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})