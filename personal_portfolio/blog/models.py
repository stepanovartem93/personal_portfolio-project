from django.db import models
from django.utils import timezone
from django.db.models.fields import CharField, DateField, TextField

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField(default='new_post')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title