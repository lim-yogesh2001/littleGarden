from django.db import models
from users.models import User
from products_category.models import Product
from datetime import timedelta, datetime
from transection.models import Payment


    
# Create your models here.
class Orders(models.Model):
    ship_time = datetime.now() + timedelta(hours=3)
    payment_id = models.ForeignKey(Payment, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default= False)
    total_amount = models.IntegerField(default=0),
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    shipping_time = models.DateTimeField(default=ship_time, editable=False, null=True)
    
    def __str__(self):
        return f"order {self.id}"
    
    class Meta:
        verbose_name_plural = "Orders"

