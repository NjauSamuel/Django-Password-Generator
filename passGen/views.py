from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello, World!</h1><br><br><br>This is the home page.")
    return render(request, "passGen/home.html")


def passGen(request):
    # Get password length from form, default to 10 if not provided
    length_str = request.GET.get('length', '10')
    try:
        length = int(length_str)
    except ValueError:
        length = 10
    
    # Build character set based on form selections
    char = list("abcdefghijklmnopqrstuvwxyz")  # Always include lowercase
    
    # Add uppercase letters if checkbox is checked
    uppercase_checked = 'uppercase' in request.GET
    if uppercase_checked:
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    # Add digits if checkbox is checked
    digits_checked = 'digits' in request.GET
    if digits_checked:
        char.extend(list("0123456789"))
    
    # Add symbols if checkbox is checked
    symbol_checked = 'symbol' in request.GET
    if symbol_checked:
        char.extend(list("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Generate password
    password = ""
    for x in range(length):
        password += random.choice(char)
    
    # Pass form parameters to template for pre-filling
    context = {
        "password": password,
        "length": length,
        "uppercase": uppercase_checked,
        "digits": digits_checked,
        "symbol": symbol_checked,
    }
    
    return render(request, "passGen/passGen.html", context)
