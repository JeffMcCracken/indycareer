from django.contrib import admin
from .models import Staff, JobPosting

class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'title',
        'order'
    ]

admin.site.register(Staff, StaffAdmin)
admin.site.register(JobPosting)
