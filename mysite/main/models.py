from django.db import models
from datetime import datetime

# Create your models here.


class PostCategory(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.title

