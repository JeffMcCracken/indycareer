from django.contrib import admin
from .models import JobPosting, Applicant

class JobPostingAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'is_active'
    ]

class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'job_posting'
    ]

admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(Applicant, ApplicantAdmin)
