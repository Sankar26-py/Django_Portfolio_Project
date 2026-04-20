from django.contrib import admin
from .models import (
    Profile, AboutHighlight, Language, Certification,
    SkillCategory, Skill, Experience, ExperienceBullet,
    Project, Education, Achievement
)


class AboutHighlightInline(admin.TabularInline):
    model  = AboutHighlight
    extra  = 1
    fields = ('text', 'order')


class LanguageInline(admin.TabularInline):
    model  = Language
    extra  = 1
    fields = ('name', 'level', 'order')


class CertificationInline(admin.TabularInline):
    model  = Certification
    extra  = 1
    fields = ('icon', 'name', 'issuer', 'order')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('👤 Personal Info', {
            'fields': ('name', 'title', 'location', 'email', 'phone', 'is_open_to_work')
        }),
        ('🎯 Hero Section', {
            'fields': ('tagline', 'tech_stack', 'bio')
        }),
        ('📊 Stats Row', {
            'fields': ('years_exp', 'perf_gain', 'automation_gain', 'api_count', 'cgpa')
        }),
        ('🔗 Links', {
            'fields': ('linkedin_url', 'github_url', 'github_project_url')
        }),
        ('📁 Files', {
            'fields': ('photo', 'resume'),
            'description': 'Upload profile photo and resume PDF here'
        }),
        ('📝 About Section — 3 Paragraphs', {
            'fields': ('about_para1', 'about_para2', 'about_para3'),
        }),
        ('☁ In Progress Card (About Sidebar)', {
            'fields': ('in_progress_title', 'in_progress_text'),
            'description': 'Leave blank to hide the In Progress card'
        }),
        ('🏢 Experience Company Header', {
            'fields': ('company_name', 'company_sub', 'company_duration'),
        }),
        ('🔻 Footer', {
            'fields': ('footer_text',)
        }),
    )
    inlines = [AboutHighlightInline, LanguageInline, CertificationInline]


class SkillInline(admin.TabularInline):
    model  = Skill
    extra  = 2
    fields = ('name', 'order')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'order')
    list_editable = ('order',)
    inlines       = [SkillInline]


class ExperienceBulletInline(admin.TabularInline):
    model  = ExperienceBullet
    extra  = 2
    fields = ('text', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ('role', 'tab_label', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_editable = ('order', 'is_current')
    inlines       = [ExperienceBulletInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'label', 'is_external', 'order')
    list_editable = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ('degree', 'school', 'period', 'cgpa', 'order')
    list_editable = ('order',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display  = ('title', 'icon', 'date_label', 'order')
    list_editable = ('order',)
