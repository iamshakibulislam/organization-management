# Generated by Django 4.0 on 2022-02-25 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0012_remove_training_categorye'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.category'),
        ),
    ]
