from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def registration(request):
    regis_errors = User.objects.registration_validation(request.POST)

    if len(regis_errors) > 0:
        for error in regis_errors:
            messages.error(request, regis_errors[error])
        return redirect('/')
    
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['regis_email']
        password = request.POST['regis_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = pw_hash)
        new_user.id = request.session['user_id']
        return redirect('/wall')


def login(request):
    login_errors = User.objects.login_validation(request.POST)

    if len (login_errors) > 0:
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
                return redirect('/wall')
            else:
                messages.error(request, "Wrong Password")
                return redirect('/')
        
        messages.error(request, "Your email does not match our records.")
        return redirect('/')

def success(request):
    if 'user_id' in request.session:
        context = {
            "user" : User.objects.get(id=request.session['user_id']),
            "all_users" : User.objects.all(),
            "all_messages" : Message.objects.all(),
            "all_comments" : Comment.objects.all(),
        }
        return render(request, 'success.html', context)
    else:
        messages.error(request, "Access Restricted, Must be signed in!")
        return redirect('/')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def post_message(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    message = request.POST['post_message']
    new_message = Message.objects.create(context=message, user=logged_user)
    new_message.save()
    return redirect('/wall')

def post_comment(request):
    comment = request.POST['post_comment']
    commenter = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=request.POST['message_id'])
    new_comment = Comment.objects.create(context=comment, user=commenter, message=message)
    new_comment.save()
    return redirect('/wall')



