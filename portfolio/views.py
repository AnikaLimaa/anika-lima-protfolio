from django.shortcuts import render



from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
# Create your views here.


def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',{'projects':projects})






