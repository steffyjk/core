from django.db import models


# Create your models here.
class AboutMe(models.Model):
    experience = models.IntegerField()
    total_projects = models.IntegerField()
    description = models.CharField(max_length=255)
