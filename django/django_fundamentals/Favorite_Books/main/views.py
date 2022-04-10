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
        request.session['user_id'] = new_user.id
        return redirect('/success')


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
                return redirect('/success')
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
            "all_books" : Book.objects.all(),
        }
        return render(request, 'books.html', context)
    else:
        messages.error(request, "Access Restricted, Must be signed in!")
        return redirect('/')

def logout(request):
    del request.session['user_id']
    print("looged Out")
    return redirect('/')

def add_book(request):
    book_errors = Book.objects.book_validation(request.POST)
    if len(book_errors) > 0:
        for error in book_errors:
            messages.error(request, book_errors[error])
            return redirect('/success')
    
    else:
        user = User.objects.get(id=request.session['user_id'])
        title = request.POST['book_title_add']
        description = request.POST['book_description_add']
        new_book = Book.objects.create(title = title, description = description, uploaded_by=user)
        new_book.save()
        user.liked_books.add(new_book)
        return redirect('/success')

def view_book(request, book_id):
    if 'user_id' in request.session:
        context = {
            "book" :  Book.objects.get(id=book_id),
            "user" : User.objects.get(id=request.session['user_id']),
            "all_books" : Book.objects.all()
        }
        return render(request, 'update.html', context)

def update_book(request, book_id):
    book_edit_errors = Book.objects.validation_book_edit(request.POST)

    if len(book_edit_errors) > 0:
        for error in book_edit_errors:
            messages.error(request, book_edit_errors[error])
        return redirect (f'/books/{book_id}')

    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['book_title_edit']
        book.description = request.POST['book_description_edit']
        book.save()
        return redirect('/success')

def delete_book(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect('/success')

def favorite(request, book_id):
    book_to_like = Book.objects.get(id=book_id)
    user_who_likes = User.objects.get(id=request.session['user_id'])
    user_who_likes.liked_books.add(book_to_like)
    user_who_likes.save()
    return redirect('/success')

def unfavorite(request, book_id):
    book_to_like = Book.objects.get(id=book_id)
    user_who_likes = User.objects.get(id=request.session['user_id'])
    user_who_likes.liked_books.remove(book_to_like)
    user_who_likes.save()
    return redirect('/success')

