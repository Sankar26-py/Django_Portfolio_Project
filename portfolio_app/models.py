from django.db import models


class Profile(models.Model):
    # ── Hero ──────────────────────────────────────────────
    name               = models.CharField(max_length=100, default="Sankar K")
    title              = models.CharField(max_length=100, default="Backend Dev.")
    tagline            = models.CharField(max_length=200, default="Available for Backend Roles")
    tech_stack         = models.CharField(max_length=300, default="Python · Django · DRF · PostgreSQL · Redis · Celery · OAuth · JWT")
    bio                = models.TextField(default="I build backend systems that scale.")
    location           = models.CharField(max_length=100, default="Chennai, Tamil Nadu, India")
    email              = models.EmailField(default="kaliyannansankar1999@gmail.com")
    phone              = models.CharField(max_length=20, default="+91-8754844723")
    linkedin_url       = models.URLField(default="https://www.linkedin.com/in/sankar-django-dev")
    github_url         = models.URLField(default="https://github.com/Sankar26-py")
    github_project_url = models.URLField(default="https://github.com/Sankar26-py/foodOnline")
    photo              = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume             = models.FileField(upload_to='resume/', blank=True, null=True)
    is_open_to_work    = models.BooleanField(default=True)
    footer_text        = models.CharField(max_length=300, default="Designed & built — Sankar K © 2026 · Python Django Developer · Chennai, India")

    # ── Stats row ─────────────────────────────────────────
    years_exp          = models.CharField(max_length=10, default="3.6+")
    perf_gain          = models.CharField(max_length=10, default="30%")
    automation_gain    = models.CharField(max_length=10, default="40%")
    api_count          = models.CharField(max_length=10, default="5+")
    cgpa               = models.CharField(max_length=10, default="9.54")

    # ── About — 3 paragraphs ──────────────────────────────
    about_para1        = models.TextField(default="Results-driven Python Backend Developer with 3.6+ years at Tata Consultancy Services, progressing from Graduate Trainee all the way to System Engineer through consistent technical delivery.")
    about_para2        = models.TextField(default="I specialise in building scalable Django REST APIs, implementing OAuth 2.0 and JWT authentication, Redis caching strategies, and designing Celery-powered async pipelines.")
    about_para3        = models.TextField(default="Currently preparing for the Microsoft Azure Developer Associate (AZ-204) certification to deepen cloud-integrated backend capabilities.")

    # ── About sidebar — In Progress card ─────────────────
    in_progress_title  = models.CharField(max_length=200, default="☁ AZ-204 — Azure Developer Associate", blank=True)
    in_progress_text   = models.TextField(default="Preparing to build cloud-integrated backend solutions on Microsoft Azure.", blank=True)

    # ── Experience company header ─────────────────────────
    company_name       = models.CharField(max_length=100, default="Tata Consultancy Services")
    company_sub        = models.CharField(max_length=150, default="Chennai, Tamil Nadu · Remote · Full-time")
    company_duration   = models.CharField(max_length=100, default="Sep 2022 – Present · 3 yrs 8 mos")

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name


class AboutHighlight(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="about_highlights")
    text    = models.CharField(max_length=300)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "About Highlight"

    def __str__(self):
        return self.text[:60]


class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="languages")
    name    = models.CharField(max_length=50)
    level   = models.CharField(max_length=50)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} — {self.level}"


class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="certifications")
    icon    = models.CharField(max_length=10, default="🐍")
    name    = models.CharField(max_length=200)
    issuer  = models.CharField(max_length=100)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name  = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name     = models.CharField(max_length=100)
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class Experience(models.Model):
    role       = models.CharField(max_length=100)
    company    = models.CharField(max_length=100)
    location   = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date   = models.CharField(max_length=50, default="Present")
    duration   = models.CharField(max_length=50)
    is_current = models.BooleanField(default=False)
    tab_label  = models.CharField(max_length=100, blank=True, help_text="Short label for the tab e.g. 'Asst. System Engineer'")
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} @ {self.company}"


class ExperienceBullet(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bullets')
    text       = models.TextField()
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:80]


class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    github_url  = models.URLField(blank=True)
    label       = models.CharField(max_length=50, blank=True)
    is_external = models.BooleanField(default=True)
    tags        = models.CharField(max_length=500, help_text="Comma-separated: Django, DRF, PostgreSQL")
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    period = models.CharField(max_length=50)
    cgpa   = models.CharField(max_length=20, blank=True)
    label  = models.CharField(max_length=50, blank=True)
    order  = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} — {self.school}"


class Achievement(models.Model):
    icon        = models.CharField(max_length=10, default="🏆")
    title       = models.CharField(max_length=200)
    description = models.TextField()
    date_label  = models.CharField(max_length=100)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class PageVisit(models.Model):
    """Tracks every visit to the portfolio"""
    timestamp  = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    referrer   = models.URLField(blank=True, max_length=500)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Page Visit"

    def __str__(self):
        return f"Visit at {self.timestamp.strftime('%Y-%m-%d %H:%M')} from {self.ip_address}"
