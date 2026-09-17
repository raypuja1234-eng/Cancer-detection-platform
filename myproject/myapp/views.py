from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def analysis(request):
    return render(request,"analysis.html")

def ourteam(request):
    return render(request,"ourteam.html")

def prediction(request):
    return render(request,"prediction.html")

def pred(request):
    radius_mean=request.POST['radius_mean']

    return HttpResponse(radius_mean)
