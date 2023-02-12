from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    print("running about")
    return render(request, 'about.html')
