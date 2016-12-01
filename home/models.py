from django.db import models

# Create your models here.

class HackathonProject(models.Models):
	internal_id = models.AutoField(primary_key=True, editable= False, primary_key=true)
	timestamp = models.DateField(default=datetime.now, blank=True,editable= False)
	title = models.CharField(maxlength=100)
	timestamp = models.DateField(default=datetime.now, blank=True,editable= False) 
	description= models.CharField(maxlength=500)
	logo = models.ImageField(upload_to='hacklogos')

	def __str__(self):
		return str(self.title)


