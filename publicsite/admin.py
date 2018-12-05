from django.contrib import admin
from .models import Staff, JobPosting

my_models = [Staff, JobPosting]
admin.site.register(my_models)
