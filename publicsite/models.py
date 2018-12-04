from django.db import models
from PIL import Image

class Staff(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    position = models.PositiveIntegerField(unique=True)
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


