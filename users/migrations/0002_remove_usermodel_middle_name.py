# Generated by Django 4.2.9 on 2024-01-03 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='middle_name',
        ),
    ]
