from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    # def _str_(self):
    #     return self.username
