from django.db import models
from users.models import User




class TourManagement(models.Model):
	member = models.ForeignKey(User,on_delete=models.CASCADE)
	last_visited = models.CharField(max_length=100,null=True,blank=True)
	next_visit_date = models.CharField(max_length=100,null=True,blank=True)
	last_meeting_date = models.CharField(max_length=100,null=True,blank=True)
	next_meeting_date = models.CharField(max_length=100,null=True,blank=True)
	tour_from = models.CharField(max_length=200,null=True,blank=True)
	tour_to = models.CharField(max_length=200,null=True,blank=True)



	def __str__(self):
		return str(self.member.first_name)+'  '+str(self.member.last_name)



