from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt 


def index(request):
    return render(request, 'index.html')


def registration(request):
    regis_erros = User.objects.registration_validation(request.POST)

    if len(regis_erros) > 0:
        for errors in regis_erros:
            messages.error(request, regis_erros[errors])
        return redirect('/')
    
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['regis_email']
        password = request.POST['regis_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = pw_hash)
        request.session['user_id'] = new_user.id
        return redirect('/success')

def login(request):
    login_errors = User.objects.login_validation(request.POST)

    if len(login_errors) > 0:
        for errors in login_errors:
            messages.error(request, login_errors[errors])
        return redirect('/')
    
    else:
        login_email = request.POST['login_email']
        user = User.objects.filter(email = login_email)
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/success')
            else:
                messages.error(request, "Wrong Password")
                return redirect('/')

        messages.error(request,"Your email does not match our recordes.")
        return redirect('/')
            
def success(request):
    if 'user_id' in request.session:
        context = {
            "user" : User.objects.get(id = request.session['user_id'])
        }
        return render(request, 'success.html', context)
    else: 
        messages.error(request, "Access Restricted, Must be signed in!")
        return redirect('/')

def logout(request):
    del request.session['user_id']
    return redirect('/')
                    