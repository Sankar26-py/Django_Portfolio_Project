import json
from django.shortcuts import render
from .models import (
    Profile, SkillCategory, Experience,
    Project, Education, Achievement, PageVisit
)


def get_client_ip(request):
    """Extract real IP even behind proxies"""
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        return x_forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def index(request):
    # Log this visit
    PageVisit.objects.create(
        ip_address = get_client_ip(request),
        user_agent = request.META.get('HTTP_USER_AGENT', '')[:500],
        referrer   = request.META.get('HTTP_REFERER', '')[:500],
    )

    profile      = Profile.objects.prefetch_related(
                       'about_highlights', 'languages', 'certifications'
                   ).first()
    skill_cats   = SkillCategory.objects.prefetch_related('skills').all()
    experiences  = Experience.objects.prefetch_related('bullets').all()
    projects     = Project.objects.all()
    educations   = Education.objects.all()
    achievements = Achievement.objects.all()

    # Build skill data as JSON for JS-driven skills section
    skill_data = [
        {'category': cat.name, 'tags': [s.name for s in cat.skills.all()]}
        for cat in skill_cats
    ]

    return render(request, 'index.html', {
        'profile':         profile,
        'skill_data_json': json.dumps(skill_data),
        'experiences':     experiences,
        'projects':        projects,
        'educations':      educations,
        'achievements':    achievements,
    })
