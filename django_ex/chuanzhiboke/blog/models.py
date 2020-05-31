from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    mobile = models.IntegerField(null=True)

    def __str__(self):
        return self.username