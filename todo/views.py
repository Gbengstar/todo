from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from .forms import *

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
