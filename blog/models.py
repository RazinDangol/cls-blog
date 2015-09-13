from django.db import models
from django.utils import timezone

# Create your models here.
# inherited from django.db.models.Model


class Blog(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Title = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    edited_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    comment_content = models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    edited_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.blog.Title
