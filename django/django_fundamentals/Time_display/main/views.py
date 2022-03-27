from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

    
def index(request):
    context = {
        "date": strftime("%Y-%m-%d"),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def back(request):
    return redirect('/')
