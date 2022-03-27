from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def blogs(request):
    return HttpResponse("Blogs")

def index(request):
    return HttpResponse("Placeholder to later display all the list of blogs.")

def root(request):
    return redirect('/')

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")

def create(request):
    return redirect('/')

def show(request, num):
    print (num)
    return HttpResponse("Placeholder to display blog number: " + num + ".")

def edit(request, num):
    print (num)
    return HttpResponse("Placeholder to edit blog " + num + ".")

def destroy(request, num):
    print (num)
    return redirect('/')

def printjson(request):
    return JsonResponse({"Title" : "My first blog", "Content" : "Lorem, impsum dolor sit amet consectetur adipisicing elit." })
