from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .input_task import TaskForm
from django import forms
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from main.form import NewUserForm
from .forms import AddTaskForm
# Create your views here.
#okay
def add_task(request):
	data=request.POST
	form= AddTaskForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj= form.save(commit=False)
		obj.user=request.user
		obj.save()
		messages.info(request, f"Task has been added")
		return redirect("todo:view_task")

	template_name='todo/create.html'
	context={'title':"Add Tasks",'form':form}

	return render (request, template_name, context)


#def view_task(request):
#okay
def view_task(request):

    tasks=Task.objects.filter(complete="False",user=request.user) 
    if len(tasks)<1:
    	messages.info(request, f"No Task has been added")
    	return redirect("todo:add_task")
    template_name='todo/list.html'
    context={'title':"Tasks not completed yet","object_list":tasks, 'x':True}
    return render (request, template_name, context)
#okay
def view_completed_task(request):

    tasks=Task.objects.filter(complete="True",user=request.user) 
    if len(tasks) <1 :
    	messages.warning(request, f"No Task has been completed")

    template_name='todo/list.html'
    context={'title':"Tasks Completed","object_list":tasks,'x':False}
    return render (request, template_name, context)
#okay
def task_completed(request,id):
	obj=Task.objects.get(id=id)
	obj.complete="True"
	obj.status="Completed"
	obj.save()
	messages.success(request, f"Congratulation! you have completed this task")
	return redirect("/view-completed-task/")


def blog_post_retrieve_view(request,id):
    obj=get_object_or_404 (Task, slug=slug) 
    template_name='todo/detail.html'
    context={"object":obj }
    return render (request, template_name, context)


def del_task(request,id):
	obj=Task.objects.get(id=id)
	obj.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def view_home(request):
	if request.user.is_authenticated:
		tasks=Task.objects.filter(user=request.user) 
		if len(tasks)<1:
			messages.info(request, f"No Task has been added")
			return redirect("todo:add_task")

		template_name='todo/list.html'
		context={"title":'All Tasks', "object_list":tasks, 'y':True}
		return render (request, template_name, context)

	return redirect("main:register")


