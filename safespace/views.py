from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def where(request):
    return render(request,'where.html')

def who(request):
    return render(request,'who.html')