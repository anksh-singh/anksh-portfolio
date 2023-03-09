from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
# from .forms import EmailForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
