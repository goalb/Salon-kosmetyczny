from django.db import models

# Create your models here.


class User(models.Model):
    login = models.CharField('login', max_length=30)
    email = models.EmailField(max_length=200)
    first_name = models.CharField('first_name', max_length=50, null=True)
    last_name = models.CharField('last_name', max_length=60, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    admin_status = models.BooleanField(default=False)

    def __str__(self):
        return self.login


class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='images/team/')
    description = models.TextField(max_length=1000, null=True, blank=True)
    admin_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    client = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='client_name')
    worker = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, limit_choices_to={'admin_status': True}, related_name='worker_name')
    date = models.DateTimeField('Appointment Date')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
