from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

def index(request):
    return render(request, 'index.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)
    return redirect('tasks:task_list')

@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task_list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('tasks:task_list')
