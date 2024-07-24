from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    keyboard_choices = [
        ('Membrana','Membrana'),
        ('Mecanico','Mecanico'),
    ]
    keyboard = models.CharField(max_length=10, choices = keyboard_choices, default='Mecanico')
    pass
