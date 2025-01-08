from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    