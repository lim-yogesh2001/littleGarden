from django.db import models
from users.models import User
from products_category.models import Product

# Create your models here.
class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default= False)
    total_amount = models.IntegerField(default=0),
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"order {self.id}"
    
    class Meta:
        verbose_name_plural = "Orders"

