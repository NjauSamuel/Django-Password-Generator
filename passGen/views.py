from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello, World!</h1><br><br><br>This is the home page.")
    return render(request, "passGen/home.html")


def passGen(request):
    char = list("abcdefghijklmnopqrstuvwxyz")
    password = ""
    for x in range(15):
        password += random.choice(char)
    
    context = {"password": password}
    
    return render(request, "passGen/passGen.html", context)
