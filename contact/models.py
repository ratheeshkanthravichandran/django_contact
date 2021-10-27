from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name    = models.CharField(max_length=125,null=True, blank=True)
    phone   = models.CharField(max_length=20)
    city    = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name, self.author) or (self.phone, self.author)