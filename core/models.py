from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=250)
    auteur = models.CharField(max_length=250)
    content = models.TextField()
    pup_date = models.DateTimeField(auto_now_add=True,)
class contact(models.Model):
    name = models.CharField(max_length=250)
    message = models.TextField()
