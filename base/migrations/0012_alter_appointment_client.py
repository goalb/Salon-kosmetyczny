# Generated by Django 4.0.6 on 2022-08-02 23:20

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_appointment_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.IntegerField(blank=True, null=True, verbose_name=base.models.User),
        ),
    ]