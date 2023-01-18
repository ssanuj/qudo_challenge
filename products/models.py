from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def clean(self):
        # Don't allow to order out of stock items.
        if self.stock_quantity <= 0:
            raise ValidationError('Out of Stock')
    class Meta:
        db_table = "Product"

class Order(models.Model):
    order_name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %Y %I:%M %p")}'