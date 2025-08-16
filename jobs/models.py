from django.db import models
from django.conf import settings
from django.utils import timezone

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    min_offer = models.DecimalField(max_digits=10, decimal_places=2 )
    max_offer = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.job_title

# Example email exactly as required: "quiz3@objor.com"

class JobApplicant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    applied_date = models.DateTimeField(default=timezone.now)
    resume = models.FileField(upload_to='resumes/')  # no renaming

    def __str__(self):
        return f"{self.user} -> {self.job}"