from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    Course.objects.create(
        Course_name = request.POST['c_name'],
        desc = request.POST['desc'] 
    )
    return redirect ('/')

def remove(request, id):
    context = {
        "course" : Course.objects.get(id=id)
    }
    return render(request, 'remove.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')