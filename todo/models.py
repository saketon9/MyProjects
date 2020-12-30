from django.db import models


# Create your models here.

priority_todo = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')

)


class todoList(models.Model):
    title = models.TextField(max_length=100)
    complated = models.BooleanField(default=True)
    priority = models.CharField(choices=priority_todo, max_length=1, default='H')