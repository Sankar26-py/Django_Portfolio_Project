from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import (
    Profile, AboutHighlight, Language, Certification,
    SkillCategory, Skill, Experience, ExperienceBullet,
    Project, Education, Achievement, PageVisit
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
            'fields': ('tagline', 'tech_stack', 'bio'),
            'description': 'Tip: wrap words in &lt;strong&gt;word&lt;/strong&gt; to make them bold'
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
            'description': 'Tip: wrap words in &lt;strong&gt;word&lt;/strong&gt; to make them bold'
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
    help_text = "Wrap phrases in <strong>text</strong> to bold them"


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


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display   = ('timestamp', 'ip_address', 'referrer_display', 'user_agent_short')
    list_filter    = ('timestamp',)
    readonly_fields = ('timestamp', 'ip_address', 'user_agent', 'referrer')
    ordering       = ('-timestamp',)

    # Remove add/delete — visits are auto-logged
    def has_add_permission(self, request):
        return False

    def referrer_display(self, obj):
        return obj.referrer[:50] if obj.referrer else '—'
    referrer_display.short_description = 'Referrer'

    def user_agent_short(self, obj):
        return obj.user_agent[:60] if obj.user_agent else '—'
    user_agent_short.short_description = 'Browser'

    def changelist_view(self, request, extra_context=None):
        """Show visitor stats summary at top of admin list"""
        now     = timezone.now()
        today   = PageVisit.objects.filter(timestamp__date=now.date()).count()
        week    = PageVisit.objects.filter(timestamp__gte=now - timedelta(days=7)).count()
        month   = PageVisit.objects.filter(timestamp__gte=now - timedelta(days=30)).count()
        total   = PageVisit.objects.count()
        unique  = PageVisit.objects.values('ip_address').distinct().count()

        extra_context = extra_context or {}
        extra_context['visitor_stats'] = {
            'today': today,
            'week':  week,
            'month': month,
            'total': total,
            'unique': unique,
        }
        return super().changelist_view(request, extra_context=extra_context)
