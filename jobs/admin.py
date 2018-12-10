from django.contrib import admin
from .models import JobPosting

class JobPostingAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'is_active'
    ]

admin.site.register(JobPosting, JobPostingAdmin)
