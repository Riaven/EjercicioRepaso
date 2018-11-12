from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'principal/index.html')

def user_list(request):
    user = User.objects.all()
    contexto = {'users':user}
    return render(request, 'registration/user_list.html', contexto)    