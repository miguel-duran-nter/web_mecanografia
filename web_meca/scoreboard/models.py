from django.db import models
from meca.models import User
from django.utils import timezone

class Scoreboard(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)