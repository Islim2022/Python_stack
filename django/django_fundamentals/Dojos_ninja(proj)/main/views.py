from django.shortcuts import render, redirect
from .models import Dojo, Ninja
def index(request):
    context = {
        "all_dojos" : Dojo.objects.all(),
        "all_ninjas" : Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def new_dojo(request):
    name = request.POST['dojo_name']
    city = request.POST['dojo_city']
    state = request.POST['dojo_state']

    Dojo.objects.create(name = name, city = city, state = state)
    return redirect('/')

def new_ninja(request):
    first_name = request.POST['ninja_f_name']
    last_name = request.POST['ninja_l_name']
    dojo = Dojo.objects.get(id=request.POST['ninja_dojo'])

    Ninja.objects.create(dojo = dojo, first_name = first_name, last_name = last_name)
    return redirect('/')

def delete(request, id):
    delete_dojo = Dojo.objects.get(id=id)
    delete_dojo.delete()

    return redirect('/')