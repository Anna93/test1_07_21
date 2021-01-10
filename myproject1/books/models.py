from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField('User name', max_length = 20)
    password = models.CharField('Password', max_length=10)
    email = models.CharField('Email', max_length=20)

    def __str__(self):
        return self.username



