from django.db import models
from reporting.models import Office

class JobPosting(models.Model):
    title = models.CharField(max_length=150)
    office = models.ForeignKey(Office, related_name='job_postings')
    status = models.CharField(max_length=150)
    expectations = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField()
    details = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Job Postings'

class Applicant(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    job_posting = models.ForeignKey(JobPosting, related_name='applicants')
    resume = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name + ' ' + self.last_name