from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Momentum!")

def login_page(request):
    return render(request, 'login/login.html')

def dashboard(request):
    return render(request, 'login/dashboard.html')
