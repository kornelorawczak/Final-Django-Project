# Generated by Django 5.0.1 on 2024-01-29 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]