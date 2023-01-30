from django.shortcuts import render
from .models import Project

# Create your views here.


def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/portfolio.html', context)
