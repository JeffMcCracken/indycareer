from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'title',
        'order'
    ]

admin.site.register(Staff, StaffAdmin)
