from django.shortcuts import render

# Create your views here.


def register(request):
    context = {

    }

    return render(request, 'member/register.html', context)