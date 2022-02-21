# Generated by Django 4.0 on 2022-02-21 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_join_date'),
        ('procurements', '0005_procurement_plan_for_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='procurement_plan_for_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('contract_package_number', models.CharField(blank=True, max_length=100, null=True)),
                ('contract_description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('estimated_price', models.FloatField(blank=True, null=True)),
                ('actual_contract_amount', models.FloatField(blank=True, null=True)),
                ('procedure_method', models.CharField(blank=True, max_length=100, null=True)),
                ('procurement_guidelines', models.CharField(blank=True, max_length=100, null=True)),
                ('prior_review', models.BooleanField(default=False)),
                ('contract_approving_authority', models.CharField(blank=True, max_length=100, null=True)),
                ('planned_date_of_ifb_publication', models.DateField(blank=True, null=True)),
                ('actual_date_of_ifb_publication', models.DateField(blank=True, null=True)),
                ('planned_date_of_bid_opening', models.DateField(blank=True, null=True)),
                ('actual_date_of_bid_opening', models.DateField(blank=True, null=True)),
                ('planned_date_of_contract_singning', models.DateField(blank=True, null=True)),
                ('actual_date_of_contract_signing', models.DateField(blank=True, null=True)),
                ('planned_date_of_delivery', models.DateField(blank=True, null=True)),
                ('actual_date_of_delivery', models.DateField(blank=True, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
