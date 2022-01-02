from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.TextField(max_length=150)
    is_completed = models.BooleanField(default=False)
