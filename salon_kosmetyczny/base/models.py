from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=200)
    first_name = models.CharField('first_name', max_length=50, null=True)
    last_name = models.CharField('last_name', max_length=60, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
