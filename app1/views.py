from django.shortcuts import render
from . import models

def home(request):
    #fetch data from Database
    data=models.SlideShow.objects.all().order_by('-id')[:1]
    return render(request,'index.html',{'data':data})
def analytics(request):
    return render(request, 'analytics.html')
