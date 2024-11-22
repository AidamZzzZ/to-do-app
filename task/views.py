from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# LISTA DE TAREAS
@login_required
def home(request):
	user_logged = request.user
	tasks = user_logged.task_set.all()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.user = request.user
			task.save()
			return redirect('home')
	else:
		form = TaskForm()

	data = {
		'tasks': tasks,
		'form':form,
	}
	return render(request, 'task/home.html', data)

# READ
@login_required
def detail_task(request, pk):
	task = get_object_or_404(Task, pk=pk)

	data = {
		'task':task,
	}

	return render(request, 'task/detail_task.html', data)

# UPDATE
@login_required
def update_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('home')

	data = {
		'form': form,
	}

	return render(request, 'task/update_task.html', data)


# DELETE
@login_required
def delete_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	if request.method == 'POST':
		task.delete()
		return redirect('home')
	return render(request, 'task/delete_task.html')

def toggle_task_status(request, pk):
	if request.method == "POST":
		task = get_object_or_404(Task, pk=pk)
		task.status = not task.status
		task.save()
	return redirect('home')