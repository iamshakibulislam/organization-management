# Generated by Django 4.0 on 2022-02-19 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_join_date'),
        ('procurements', '0002_procurement_plan_for_goods_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='procurement_plan_for_goods',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
