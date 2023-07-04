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


class WorkCategory(models.Model):
    name = models.CharField(max_length=255)


class MyWork(models.Model):
    work_category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Myinfo(models.Model):
    plateform_name = models.CharField(max_length=255)
    plateform_id = models.CharField(max_length=255)
    plateform_link = models.CharField(max_length=255)


class ContactMe(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(max_length=400)
