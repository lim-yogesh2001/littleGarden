from django.db import models
from users.models import User
from order.models import Orders
from products_category.models import Product

# Create your models here.

class Payment(models.Model):
    payment_type = models.CharField(max_length=100)

    def __str__(self):
        return f"payment {self.id}"
    

class Transection(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"transection {self.id}"
    