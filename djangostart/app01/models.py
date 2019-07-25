from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=18)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=32)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username