import imp
from django.db import models


class procurement_plan_for_goods(models.Model):
    contract_package_number = models.CharField(max_length=100,null=True,blank=True)
    contract_description = models.CharField(max_length=100,null=True,blank=True)
    unit = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    estimated_price = models.FloatField(null=True,blank=True)
    actual_contract_amount = models.FloatField(null=True,blank=True)
    procedure_method = models.CharField(max_length=100,null=True,blank=True)
    procurement_guidelines = models.CharField(max_length=100,null=True,blank=True)
    prior_review = models.BooleanField(default=False)
    contract_approving_authority = models.CharField(max_length=100,null=True,blank=True)
    planned_date_of_ifb_publication = models.DateField(auto_now=False,blank=True,null=True)
    actual_date_of_ifb_publication = models.DateField(auto_now=False,blank=True,null=True)
    planned_date_of_bid_opening = models.DateField(auto_now=False,blank=True,null=True)
    actual_date_of_bid_opening = models.DateField(auto_now=False,blank=True,null=True)
    planned_date_of_contract_singning = models.DateField(auto_now=False,blank=True,null=True)
    actual_date_of_contract_signing = models.DateField(auto_now=False,blank=True,null=True)
    planned_date_of_delivery = models.DateField(auto_now=False,blank=True,null=True)
    actual_date_of_delivery = models.DateField(auto_now=False,blank=True,null=True)
    supplier_name = models.CharField(max_length=100,null=True,blank=True)
    remarks = models.CharField(max_length=100,null=True,blank=True)
    organization = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.contract_package_number)




