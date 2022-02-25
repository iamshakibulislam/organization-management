from email.policy import default
from django.db import models
from users.models import User

class category(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name

class training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    organization = models.CharField(max_length=100,null=True)
    po_name = models.CharField(max_length=200, default='',null=True, blank=True)
    sub_sector = models.CharField(max_length=200, default='',null=True, blank=True)
    budget_head = models.CharField(max_length=200, default='',null=True, blank=True)
    sub_budget_head1 = models.CharField(max_length=200, default='',null=True, blank=True)
    training_title = models.CharField(max_length=500, default='',null=True, blank=True)
    training_topic = models.CharField(max_length=500, default='',null=True, blank=True)
    
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    budget = models.FloatField(default=0,null=True, blank=True)
    cost = models.FloatField(default=0,null=True, blank=True)
    date = models.DateField(auto_now_add=True,null=True, blank=True)
    duration = models.CharField(max_length=200, default='',null=True, blank=True)
    batch = models.CharField(max_length=200, default='',null=True, blank=True)
    total_session_conducted = models.IntegerField(default=0,null=True, blank=True)
    no_of_facilitator_official = models.IntegerField(default=0,null=True, blank=True)
    no_of_facilitator_private = models.IntegerField(default=0,null=True, blank=True)
    no_of_facilitator_internal = models.IntegerField(default=0,null=True, blank=True)

    information_of_facilitator_official_name = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_official_designation = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_official_organization = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_official_contact = models.CharField(max_length=500, default='',null=True, blank=True)

    information_of_facilitator_private_name = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_private_designation = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_private_organization= models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_private_contact = models.CharField(max_length=500, default='',null=True, blank=True)

    information_of_facilitator_internal_name = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_internal_designation = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_internal_organization = models.CharField(max_length=500, default='',null=True, blank=True)
    information_of_facilitator_internal_contact = models.CharField(max_length=500, default='',null=True, blank=True)
    total_number_of_trainer = models.IntegerField(default=0,null=True, blank=True)

    po_male_perticipent = models.CharField(max_length=500, default='',null=True, blank=True)
    po_female_perticipent = models.CharField(max_length=500,default='',null=True,blank=True)
    po_total_perticipent = models.IntegerField(default=0,null=True,blank=True)

    me_male_perticipent = models.CharField(null=True,blank=True,max_length=400)
    me_female_perticipent = models.CharField(max_length=400,blank=True,null=True)
    me_total_perticipent = models.IntegerField(default=0,blank=True,null=True)

    other_male_perticipent = models.CharField(null=True,blank=True,max_length=400)
    other_female_perticipent = models.CharField(max_length=400,blank=True,null=True)
    other_total_perticipent = models.IntegerField(default=0,blank=True,null=True)

    total_perticipent = models.IntegerField(default=0,blank=True,null=True)


    def __str__(self):
        return self.training_title



