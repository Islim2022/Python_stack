from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0: 
        for key, error in errors.items():
            messages.error(request, error)
        return redirect("/shows/new")

    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['nwork'],
        release_date = request.POST['rdate'],
        description = request.POST['desc']
    )
    return redirect(f"/shows/{show.id}")

def update_show(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, error in errors.items():
            messages.error(request, error)
        return redirect(f"/shows/{show_id}/edit")

    updated_show = Show.objects.get(id=show_id)
    updated_show.title = request.POST['title']
    updated_show.network = request.POST['nwork']
    updated_show.release_date = request.POST['rdate']
    updated_show.description = request.POST['desc']
    updated_show.save()
    return redirect(f"/shows/{show_id}")

def delete(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect("/shows")
