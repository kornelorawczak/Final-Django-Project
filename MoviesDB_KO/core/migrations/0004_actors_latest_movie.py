# Generated by Django 5.0.1 on 2024-01-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_remove_actors_surname_remove_directors_surname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='latest_movie',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
