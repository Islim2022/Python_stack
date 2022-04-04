from django.shortcuts import render, redirect, HttpResponse
from .models import *

def shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def add_show(request):
    return render(request, 'add_a_new_show.html')

def edit_show(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)

def show_summary(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'tv_show.html', context)

def create(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['nwork'],
        release_date = request.POST['rdate'],
        description = request.POST['desc']
    )
    return redirect("/shows")

def update_show(request):
    updated_show = Show.objects.get(id=request.POST['id'])
    updated_show.title = request.POST['title']
    updated_show.network = request.POST['nwork']
    updated_show.release_date = request.POST['rdate']
    updated_show.description = request.POST['desc']
    updated_show.save()
    return redirect("/shows")

def delete(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect("/shows")
