from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=225)
    network = models.CharField(max_length=225)
    release_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
