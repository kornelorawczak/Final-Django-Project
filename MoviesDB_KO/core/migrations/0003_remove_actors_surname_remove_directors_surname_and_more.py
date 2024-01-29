# Generated by Django 5.0.1 on 2024-01-07 02:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_rename_director_id_movies_director_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='directors',
            name='surname',
        ),
        migrations.AlterField(
            model_name='actors',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='actors',
            name='name',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AlterField(
            model_name='directors',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='directors',
            name='latest_movie',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='directors',
            name='name',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AlterField(
            model_name='movies',
            name='academy_awards',
            field=models.SmallIntegerField(
                default=' ',
                validators=[django.core.validators.MinValueValidator(
                    0), django.core.validators.MaxValueValidator(11)],
            ),
        ),
        migrations.AlterField(
            model_name='movies',
            name='director',
            field=models.ForeignKey(
                default=' ',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='movies',
                to='core.directors',
            ),
        ),
        migrations.AlterField(
            model_name='movies',
            name='lead_actor',
            field=models.ForeignKey(
                default=' ',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='movies',
                to='core.actors',
            ),
        ),
        migrations.AlterField(
            model_name='movies',
            name='premiere_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
