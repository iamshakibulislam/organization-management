# Generated by Django 4.0 on 2022-02-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_has_procurement_perm_user_has_tour_perm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_delete_perm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='has_edit_perm',
            field=models.BooleanField(default=False),
        ),
    ]
