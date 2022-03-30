import http
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is User_shell')
