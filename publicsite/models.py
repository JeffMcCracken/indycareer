from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image

class Staff(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    order = models.PositiveIntegerField(unique=True)
    photo = models.ImageField(upload_to='media/staff_headshots')

    def __str__(self):
        return self.name

    def save(self):
        if not self.photo:
            return
        
        super(Staff, self).save()
        image = Image.open(self.photo)
        (width, height) = image.size
        size = (round(width*.25), round(height*.25))
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)

    class Meta:
        verbose_name_plural = 'Staff'

class JobPosting(models.Model):
    title = models.CharField(max_length=150)
    office = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    expectations = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField()
    details = models.TextField()
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Job Postings'


