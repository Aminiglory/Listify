from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request,"listify/auth/login.html")

def register(request):
    return render(request,"listify/auth/register.html")

def index(request):
    return render(request,"listify/index.html")

def dashboard(request):
    return render(request,"listify/dashboard.html")

def createTask(request):
    return render(request,"listify/create.html")

def displayAllTasks(request):
    return render(request,"listify/display.html")

def viewTask(request):
    return render(request,"listify/view.html")

def editTask(request):
    return render(request,"listify/edit.html")

def deleteTask(request):
    return render(request,"listify/delete.html")