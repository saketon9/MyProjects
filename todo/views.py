from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def todo(request):
    tasks = todoList.objects.all()
    form = todo_app()
    if request.method == 'POST':
        form = todo_app(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo.html', context)


def update_todo(request, pk):
    task = todoList.objects.get(id=pk)
    form = todo_app(instance=task)
    if request.method == 'POST':
        form = todo_app(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'update_todo.html', context)






