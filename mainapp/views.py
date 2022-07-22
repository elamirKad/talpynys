from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tasks(request):
    dictionary = {
        'test': 'Test'
    }
    return render(request, 'tasks.html', dictionary)