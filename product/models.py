from django.db import models
from category.models import CategoryModel
from cloudinary.models import CloudinaryField

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=20)
	category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
	description = models.CharField(max_length=50)
	attribute = models.CharField(max_length=20)
	currency = models.CharField(max_length=5, default='Rs.')
	discount = models.IntegerField(default=0)
	price = models.IntegerField()
	#image = models.ImageField()
	image = CloudinaryField('image')
	homepage = models.BooleanField(default=False)
	is_new = models.BooleanField(default=False)

	def __str__(self):
		return self.name


