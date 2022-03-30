from django.shortcuts import render, redirect
from .models import User

def index(request):

    context = {
        "all_the_users" : User.objects.all()
    }
    return render (request, 'index.html', context)

def add_user(request):
    if request.method == "POST":
    
        last_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address = request.POST['email'], age = request.POST['age'])
        last_user.save()

    print(last_user)
    return redirect('/')

def reset(request):
    if request.method == 'POST':
        all_users = User.objects.all()
        all_users.delete()
    return redirect('/')

    
