# Generated by Django 3.0.4 on 2020-09-19 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200919_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='Limit',
        ),
    ]