from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("This is about view")
def contact(request):
    return HttpResponse("This is contact view")
def login(request):
    return render(request,"login.html")