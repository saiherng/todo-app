from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views here.

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
                'tasks' : tasks,
                'form' : form
                }

    return render(request, 'tasks/task_list.html', context)


def delete_task(request, task_id):
    task_to_delete = Task.objects.get(id=task_id )
    task_to_delete.delete()

    return redirect('/')
