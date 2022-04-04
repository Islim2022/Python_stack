from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, POST_data):
        errors = {}

        if len(POST_data["title"]) < 2:
            errors["title"] = "Please enter title at least 2 characters."
        if len(POST_data["nwork"]) < 2:
            errors["nwork"] = "Please enter a network at least 2 characters."
        if len(POST_data["desc"]) < 10:
            errors["desc"] = "Please enter a description at more than 10 characters."

        return errors

class Show(models.Model):
    title = models.CharField(max_length=225)
    network = models.CharField(max_length=225)
    release_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()