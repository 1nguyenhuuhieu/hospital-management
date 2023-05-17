from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from account.models import *
from django.shortcuts import get_object_or_404


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
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect("news:index")

            else:
                return redirect("news:index")
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'account/register-email.html', context)

def profile(request):
    user = request.user
    user = get_object_or_404(User, pk=user.id)
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = Profile(user=user)
        profile.save()

    if request.method == "POST" and 'update_profile' in request.POST:
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account:profile")
    else:
        profile_form = ProfileForm(instance=profile)

    form = UserForm(instance=user)

    context = {
        'profile': profile,
        'form': form,
        'profile_form': profile_form
    }

    return render(request, 'account/profile.html', context)




