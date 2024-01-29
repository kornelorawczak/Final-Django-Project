# Generated by Django 5.0.1 on 2024-01-14 23:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0009_alter_movies_premiere_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='academy_awards',
            field=models.SmallIntegerField(
                default=None,
                null=True,
                validators=[django.core.validators.MinValueValidator(
                    0), django.core.validators.MaxValueValidator(11)],
            ),
        ),
        migrations.AlterField(
            model_name='movies',
            name='premiere_date',
            field=models.DateField(default=None, null=True),
        ),
    ]