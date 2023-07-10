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

    def __str__(self):
        return f"{self.description}"


class ExperienceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class ExperienceTechnology(models.Model):
    exp_cat_id = models.ForeignKey(ExperienceCategory, on_delete=models.CASCADE)
    tech_name = models.CharField(max_length=255)
    tech_qualification = models.CharField(max_length=45, choices=QUALIFICATION_CHOICES)

    def __str__(self):
        return f"{self.tech_name}"


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sub_service}"


class WorkCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class MyWork(models.Model):
    work_category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.description}"


class Myinfo(models.Model):
    plateform_name = models.CharField(max_length=255)
    plateform_id = models.CharField(max_length=255)
    plateform_link = models.CharField(max_length=255)

    def __str__(self):
        return f"name: {self.plateform_name} | id: {self.plateform_id}"


class ContactMe(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(max_length=400)

    def __str__(self):
        return f"name: {self.name} | email: {self.email} | desc: {self.description}"


class Testimonial(models.Model):
    testimonial_provider_name = models.CharField(max_length=150)
    profile_pic = models.CharField(max_length=150)
    review_text = models.CharField(max_length=255)

    def __str__(self):
        return f"name: {self.testimonial_provider_name} | review_text: {self.review_text}"
