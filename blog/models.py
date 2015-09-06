from django.db import models

# Create your models here.
#inherited from django.db.models.Model
class Blog(models.Model):
    content=models.TextField()
    