import json
from django.shortcuts import render
from .models import (
    Profile, SkillCategory, Experience,
    Project, Education, Achievement
)


def index(request):
    profile      = Profile.objects.prefetch_related(
                       'about_highlights', 'languages', 'certifications'
                   ).first()
    skill_cats   = SkillCategory.objects.prefetch_related('skills').all()
    experiences  = Experience.objects.prefetch_related('bullets').all()
    projects     = Project.objects.all()
    educations   = Education.objects.all()
    achievements = Achievement.objects.all()

    # Build skill data as JSON for the JS-driven skills section
    skill_data = [
        {
            'category': cat.name,
            'tags': [s.name for s in cat.skills.all()]
        }
        for cat in skill_cats
    ]

    return render(request, 'index.html', {
        'profile':      profile,
        'skill_data_json': json.dumps(skill_data),
        'experiences':  experiences,
        'projects':     projects,
        'educations':   educations,
        'achievements': achievements,
    })
