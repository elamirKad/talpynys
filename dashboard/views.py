from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ProfilePic, AccountExperience
from talpynys.levelcalc import calculate_level


# Create your views here.
def dashboard(request, username):
    account = User.objects.get(username=username)
    exp = AccountExperience.objects.get(username=account)
    dictionary = {
        'username': account.username,
        'first_name': account.first_name,
        'last_name': account.last_name,
        'email_address': account.email,
        'experience': exp.experience,
        'level': calculate_level(exp.experience)
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
        'last_name': account.last_name,
        'email_address': account.email
    }
    if request.method == "POST":
        if 'pfpbutton' in request.POST:
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
            return redirect('/dashboard/settings/')
        elif 'namebutton' in request.POST:
            account.first_name = request.POST.get('first_name')
            account.last_name = request.POST.get('last_name')
            account.save()
            return redirect('/dashboard/settings/')
        elif 'emailbutton' in request.POST:
            account.email = request.POST.get('email')
            account.save()
            return redirect('/dashboard/settings/')
    else:
        return render(request, 'settings.html', dictionary)