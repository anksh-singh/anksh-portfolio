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


# def email_form(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             send_mail('New Email Submission', email, 'from@example.com', ['to@example.com'])
#             return render(request, 'success.html')
#     else:
#         form = EmailForm()

#     return render(request, 'email_form.html', {'form': form})
