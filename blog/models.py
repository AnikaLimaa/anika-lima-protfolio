from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    title=models.CharField(max_length=50)
    currentdate = models.DateField(default=timezone.now)
    description=models.CharField(max_length=200)



    def __str__(self):
        return self.title