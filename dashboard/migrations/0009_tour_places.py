# Generated by Django 4.0 on 2022-01-31 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_tourmanagement_comment_tourmanagement_sub_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='tour_places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.tourmanagement')),
            ],
        ),
    ]
