from django.contrib import admin
from .models import Office

class OfficeAdmin(admin.ModelAdmin):
    list_display = [
        'city',
        'street_address',
        'zip_code',
        'phone'
    ]

admin.site.register(Office, OfficeAdmin)
