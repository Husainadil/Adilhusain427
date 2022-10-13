from turtle import right
from django.shortcuts import HttpResponse, render

# Create your views here.

def home(request):
    return render(request, "portfolio/home.html")


def about(request):
    return HttpResponse("Hello Adil Wellcome to the world of Django")




def contact(request):
    return HttpResponse("Hello, Adil You want to became Data Scienctist")







