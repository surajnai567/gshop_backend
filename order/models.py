from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from product.models import Product

choices = (
	('deliver', 'Delivered'),
	('Pending', 'Pending'),
	('On Way', 'On the Way'),
	('Canceled', 'Canceled')
)


class Order(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=10)
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(choices=choices, max_length=10, default=choices[1][0])
	totalamount = models.CharField(max_length=10)
	mobile = models.CharField(max_length=12)
	area = models.CharField(max_length=20)
	address = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id)


class OrderDetail(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	itemname = models.CharField(max_length=15)
	itemquantity = models.CharField(max_length=10)
	attribute = models.CharField(max_length=10)
	currency = models.CharField(max_length=10)
	itemImage = models.CharField(max_length=20)
	itemprice = models.CharField(max_length=10)
	itemtotal = models.CharField(max_length=10)
	date = models.DateField(auto_now_add=True)
	total = models.CharField(max_length=10)
	status = models.CharField(max_length=10)


	def __str__(self):
		return str(self.order_id)







