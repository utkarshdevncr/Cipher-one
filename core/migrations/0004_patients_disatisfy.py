# Generated by Django 3.0.4 on 2020-09-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200919_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='Disatisfy',
            field=models.CharField(default='', max_length=100),
        ),
    ]