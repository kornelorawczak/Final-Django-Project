# Generated by Django 5.0.1 on 2024-01-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0007_alter_actors_name_alter_directors_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='directors',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
