from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'hospital_quality_management/index.html', {})

def evaluation_criteria(request):
    sections = Section.objects.all()

    context = {
        'sections': sections
    }
    return render(request, 'hospital_quality_management/evaluation-criteria.html', context)