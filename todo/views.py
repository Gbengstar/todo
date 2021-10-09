#from django.http import request
#from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(request):
    todo = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context= {'todo': todo, "form": form}
    return render(request,'home.html', context)

def update(request,pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'update.html', context)

def delete(request,pk):
    items = Todo.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('/')

    context = {'items': items}
    return render(request, 'delete.html', context )


def register (request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username , password= password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            messages.info(request, "supply correct info")

    return render(request, 'login.html')