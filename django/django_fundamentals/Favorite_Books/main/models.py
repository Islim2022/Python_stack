from django.db import models
import re

class UserManager(models.Manager):
    def registration_validation(self, POSTData):
        errors = {}
        if len(POSTData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(POSTData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(POSTData['regis_email']):
            errors['regis_email'] = "Invalid Email Address!"
        check_email = User.objects.filter(email = POSTData['regis_email'])
        if len(check_email) > 0:
            errors['regis_email'] = "This email is already registered"
        if len(POSTData['regis_password']) < 7:
            errors['regis_password'] = "Password is too short! Needs to be at least 8 characters in length"
        if POSTData['confirm_regis_password'] != POSTData['regis_password']:
            errors['confirm_regis_password'] = "Passwords do not match!"
        return errors

    def login_validation(self, POSTData):
        errors = {}
        if len(POSTData['login_email']) <= 0:
            errors['login_email'] = "Please submit your email"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(POSTData['login_email']):
            errors['login_email'] = "Invalid Email Address!"
        if len(POSTData['login_password']) <= 0:
            errors['login_password'] = "Please submit your password!"
        return errors

class BookManager(models.Manager):
    def book_validation(self, POSTData):
        errors = {}
        if len(POSTData['book_title_add']) < 6:
            errors['book_title_add'] = "The book title should be at least 5 characters"
        if len(POSTData['book_description_add']) <= 6:
            errors['book_description_add'] = "Please add a book description that is at least 5 characters"
        return errors

    def validation_book_edit(self, POSTData):
        errors = {}
        if len(POSTData['book_title_edit']) < 6:
            errors['book_title_edit'] = "The book title should be at least 5 characters"
        if len(POSTData['book_description_edit']) <= 6:
            errors['book_description_edit'] = "Please add a book description that is at least 5 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    # books_uploaded = a list of books uploaded by a given user.
    # liked_books = a list of books a given user likes.

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
