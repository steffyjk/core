from django.contrib import admin
from .models import AboutMe, ExperienceTechnology, ExperienceCategory

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(ExperienceTechnology)
admin.site.register(ExperienceCategory)
