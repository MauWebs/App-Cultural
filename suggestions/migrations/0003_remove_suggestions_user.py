# Generated by Django 4.2.6 on 2023-11-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='user',
        ),
    ]
