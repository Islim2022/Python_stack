from django.db import models
import re

class UserManager(models.Manager):
    def registration_validation(self, POSTData):
        errors = {}
        if len (POSTData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(POSTData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(POSTData['regis_email']):
            errors['regis_email'] = "Invalid Email Address!"

        # Checking if there is an existing email
        check_email = User.objects.filter(email=POSTData['regis_email'])
        if len(check_email) > 0:
            errors['regis_email'] = "This email is already registered"
        
        if len(POSTData['regis_password']) <= 0:
            errors['regis_password'] = "Please submit a password!"
        if POSTData['regis_password'] != POSTData['confirm_regis_password']:
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
            errors['login_password'] = "Please submit a password!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
