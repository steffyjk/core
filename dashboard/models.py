from django.db import models

# Create your models here.
QUALIFICATION_CHOICES = (
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
)


class AboutMe(models.Model):
    experience = models.IntegerField()
    total_projects = models.IntegerField()
    description = models.CharField(max_length=255)


class ExperienceCategory(models.Model):
    name = models.CharField(max_length=100)


class ExperienceTechnology(models.Model):
    exp_cat_id = models.ForeignKey(ExperienceCategory, on_delete=models.CASCADE)
    tech_name = models.CharField(max_length=255)
    tech_qualification = models.CharField(max_length=45, choices=QUALIFICATION_CHOICES)


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service = models.CharField(max_length=255)
