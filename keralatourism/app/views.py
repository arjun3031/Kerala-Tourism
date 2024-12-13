from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request,'homepage.html')

def district(request):
    return render(request,'district.html')

def services(request):
    return render(request,'services.html')

def contactus(request):
    return render(request,'contactus.html')