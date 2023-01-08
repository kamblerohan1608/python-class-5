from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def education(request):
    return render(request,'education.html')

def skills(request):
    return render(request,'skills.html')

def exp(request):
    return render(request,'exp.html')

def contact(request):
    return render(request,'contact.html')


