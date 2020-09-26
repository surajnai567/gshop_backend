from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=15)
    #url = models.ImageField()
    image = CloudinaryField('image')

