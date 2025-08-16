from django.contrib import admin
from .models import Job, JobApplicant

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("job_title", "location", "min_offer", "max_offer")
    search_fields = ("job_title", "job_description", "location")

@admin.register(JobApplicant)
class JobApplicantAdmin(admin.ModelAdmin):
    list_display = ("user", "job", "applied_date")
    search_fields = ("user__username", "job__job_title")
