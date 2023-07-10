from django.contrib import admin
from .models import (AboutMe, ExperienceTechnology, ExperienceCategory, Service, SubService, WorkCategory, MyWork,
                     Myinfo, ContactMe, Testimonial)

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(ExperienceTechnology)
admin.site.register(ExperienceCategory)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(WorkCategory)
admin.site.register(Myinfo)
admin.site.register(MyWork)
admin.site.register(ContactMe)
admin.site.register(Testimonial)
