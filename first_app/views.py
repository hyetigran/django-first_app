from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me': "Hello I'm from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)


def help(request):
    help_dict = {'help_me': 'hello from views.py'}
    return render(request, 'first_app/help.html', context=help_dict)
