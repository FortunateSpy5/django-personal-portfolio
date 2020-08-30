from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(default=now())
    content = models.TextField()
