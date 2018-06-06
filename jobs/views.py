from django.shortcuts import render
from .models import Job

def home(request):
    # django will automatically search the templates folder
    # the reason we need the subfolder jobs is to differenciate in case there are home.thml file in another app
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
