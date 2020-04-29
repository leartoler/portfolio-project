from django.db import models

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=100)
	pub_date=models.DateField()
	body=models.TextField()
	image=models.ImageField(upload_to='images/')

	def __str__(self): #éste sirve para cuando se quiera modificar algo en el propio admin
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
		