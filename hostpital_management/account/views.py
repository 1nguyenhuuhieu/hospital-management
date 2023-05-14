from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register(request):
    context = {

    }

    return render(request, 'account/register.html', context)

def register_email(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    


    return render(request, 'account/register-email.html', context)