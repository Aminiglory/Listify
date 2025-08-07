from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request,"listify/auth/login.html")

def register(request):
    return render(request,"listify/auth/register.html")

def index(request):
    return render(request,"listify/index.html")