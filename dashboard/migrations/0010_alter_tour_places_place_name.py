# Generated by Django 4.0 on 2022-01-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_tour_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour_places',
            name='place_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
