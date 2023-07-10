from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import AboutMe, ExperienceTechnology, ExperienceCategory, Service, WorkCategory, Myinfo, Testimonial


def home(request):
    about_me = AboutMe.objects.first()
    exp_techs = ExperienceTechnology.objects.all()
    exp_cats = ExperienceCategory.objects.all()
    experience = {f"{i.name}": [] for i in exp_cats}
    for exp_cat in exp_cats:

        for exp_tech in exp_techs:
            if exp_tech.exp_cat_id.id == exp_cat.id:
                experience[f"{exp_cat.name}"].append({
                    "tech_name": exp_tech.tech_name,
                    "tech_qualification": exp_tech.tech_qualification
                })
    categories = ExperienceCategory.objects.all()
    services = Service.objects.all()
    work_categories = WorkCategory.objects.all()
    my_info = Myinfo.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "about_me": about_me,
        "categories": categories,
        "services": services,
        "work_categories": work_categories,
        "my_info": my_info,
        "testimonials": testimonials
    }
    return render(request, 'index.html', context=context)
