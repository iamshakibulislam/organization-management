from django.db import models
from users.models import User




class TourManagement(models.Model):
	tourstatus = [('pending approval','pending approval'),
				('approved','approved'),
				('finished','finished')
	]

	date = models.DateField(auto_now_add=True,null=True)
	tour_members = models.ManyToManyField(User,through='tour_member_data')
	organization = models.CharField(max_length=200,null=True,blank=False)
	last_visited = models.CharField(max_length=100,null=True,blank=True)
	next_visit_date = models.CharField(max_length=100,null=True,blank=True)
	last_meeting_date = models.CharField(max_length=100,null=True,blank=True)
	next_meeting_date = models.CharField(max_length=100,null=True,blank=True)
	tour_from = models.CharField(max_length=200,null=True,blank=True)
	tour_to = models.CharField(max_length=200,null=True,blank=True)
	sub_sector = models.CharField(max_length=100,null=True,blank=True)
	comment = models.CharField(max_length=500,null=True,blank=True)
	status = models.CharField(max_length=90,default='pending approval',choices=tourstatus,blank=True)

	def __str__(self):
		return str(self.tour_from)+' '+str(self.tour_to)





class tour_member_data(models.Model):
	member = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	tour = models.ForeignKey(TourManagement,on_delete=models.CASCADE,null=True)


	def __str__(self):
		return str(self.member.first_name)




class tour_files(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
	tour = models.ForeignKey(TourManagement,on_delete=models.CASCADE,null=False,blank=False)
	file = models.FileField(upload_to='tour/')


	def __str__(self):
		return str(self.user.first_name)


