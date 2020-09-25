from django.db import models

# Create your models here.
class CategoryModel(models.Model):
	categry = models.CharField(max_length=15)
	cateimg = models.ImageField()

	def __str__(self):
		return self.categry

