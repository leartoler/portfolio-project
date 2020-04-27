from django.contrib import admin
#Lo que aparecerá en el admin
from .models import Job
admin.site.register(Job)