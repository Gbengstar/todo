from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Todo(models.Model):
    task= models.CharField(max_length=100, null=False)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['date']

    
