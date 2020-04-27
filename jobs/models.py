from django.db import models

# Classn job, en 2: image, que son imágenes, y summary, que es lo que 
#irá escrito
class Job(models.Model):
	image=models.ImageField(upload_to='images/')
	summary=models.CharField(max_length=200)
 