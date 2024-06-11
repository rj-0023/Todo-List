from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskModel
from .forms import TaskForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(f'{username} - {password}')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Registration Successfull")
                return redirect("Data")
            
    else:
        form = RegisterUserForm()
    context={
        "form":form,
    }
    return render(request, 'register_user.html', context)

def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(f"{username} - {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Data")
        else:
            messages.error(request, message="Invalid credentials")
            return redirect("login")
    else:
        
        context={

        }
        return render(request, "login.html", context) 

def logout_user(request):
    logout(request)
    messages.success(request, message="User logged out")
    return redirect("login")


@login_required
def dataview(request):
    obj = TaskModel.objects.filter(user=request.user)
    context = {
        "tasks": obj,
    }
    # return HttpResponse("<h1>Index View</h1>")

    return render(request, "data.html", context)  


@login_required
def dynamicview(request, id):
    obj = TaskModel.objects.get(id=id) 
    context = {
        "tasks": obj,
    }
    # return HttpResponse("<h1>Index View</h1>")
    return render(request, "dynamic.html", context)  

@login_required
def deleteview(request, id):
    obj = TaskModel.objects.get(id=id) 
    if request.method == "POST":
        print(request.POST)
        obj.delete()
        return redirect('../../')
    context = {
        "tasks": obj,
    }
    # return HttpResponse("<h1>Index View</h1>")
    return render(request, "delete.html", context)  

@login_required
def updateview(request, id):
    obj = TaskModel.objects.get(id=id) 
    form = TaskForm(request.POST or None, instance=obj) 
    if form.is_valid():
        form.save()
        return redirect('Data')
    context = {
        "tasks": obj,
        "form": form,
    }
    return render(request, "edit.html", context)


@login_required
def formview(request):
    form = TaskForm(request.POST or None) 
    print(form.errors)

    if form.is_valid():
        form.save()
        print(form.errors)

        form = TaskForm()
    context = {
        "form": form,
    }
    # return HttpResponse("<h1>Index View</h1>")
    return render(request, "form.html", context)  

def index(request):
    return render(request, "index.html")  
