from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.core.mail import send_mail
# from .forms import EmailForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def submit_email(request):
    # return HttpResponse('Thank you for contacting us!')
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_mail(
            'New email submission',
            f'The following email was submitted: {email}',
            '',
            [''],
            fail_silently=False,
        )
            #return render(request, 'success.html')
    else:
        form = EmailForm()

#     return render(request, 'email_form.html', {'form': form})
    return  HttpResponse("Thank you for contacting me!")
