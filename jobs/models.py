from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=150)
    office = models.CharField(max_length=150)
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
