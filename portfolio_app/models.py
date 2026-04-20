from django.db import models


class Profile(models.Model):
    """Hero section & general info — edit everything from admin"""
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
    footer_text        = models.CharField(max_length=200, default="Designed & built — Sankar K © 2026 · Python Django Developer · Chennai, India")

    # Stats row
    years_exp          = models.CharField(max_length=10, default="3.6+")
    perf_gain          = models.CharField(max_length=10, default="30%")
    automation_gain    = models.CharField(max_length=10, default="40%")
    api_count          = models.CharField(max_length=10, default="5+")
    cgpa               = models.CharField(max_length=10, default="9.54")

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name


class AboutHighlight(models.Model):
    """Bullet points in the About section"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="about_highlights")
    text    = models.CharField(max_length=300)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "About Highlight"

    def __str__(self):
        return self.text[:60]


class Language(models.Model):
    """Languages card in about sidebar"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="languages")
    name    = models.CharField(max_length=50)
    level   = models.CharField(max_length=50)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} — {self.level}"


class Certification(models.Model):
    """Certifications card in about sidebar"""
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
    """Each skill group in the Skills section"""
    name  = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Individual skill tag within a category"""
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name     = models.CharField(max_length=100)
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class Experience(models.Model):
    """Each role/tab in the Experience section"""
    role       = models.CharField(max_length=100)
    company    = models.CharField(max_length=100)
    location   = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date   = models.CharField(max_length=50, default="Present")
    duration   = models.CharField(max_length=50)
    is_current = models.BooleanField(default=False)
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} @ {self.company}"


class ExperienceBullet(models.Model):
    """Bullet point under each experience role"""
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bullets')
    text       = models.TextField()
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:80]


class Project(models.Model):
    """Cards in the Projects section"""
    title       = models.CharField(max_length=200)
    description = models.TextField()
    github_url  = models.URLField(blank=True)
    label       = models.CharField(max_length=50, blank=True, help_text="e.g. 'GitHub →' or 'SRMIST Thesis'")
    is_external = models.BooleanField(default=True, help_text="If False, shows as muted label (no link)")
    tags        = models.CharField(max_length=500, help_text="Comma-separated: Django, DRF, PostgreSQL")
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Education(models.Model):
    """Cards in the Education section"""
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    period = models.CharField(max_length=50)
    cgpa   = models.CharField(max_length=20, blank=True)
    label  = models.CharField(max_length=50, blank=True, help_text="e.g. 'Online Degree'")
    order  = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} — {self.school}"


class Achievement(models.Model):
    """Cards in the Achievements section"""
    icon        = models.CharField(max_length=10, default="🏆")
    title       = models.CharField(max_length=200)
    description = models.TextField()
    date_label  = models.CharField(max_length=100)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
