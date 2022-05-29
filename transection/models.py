from django.db import models
from users.models import User

# Create your models here.

class Payment(models.Model):
    payment_type = models.CharField(max_length=100)

    def __str__(self):
        return f"payment {self.id}"
    

class Transection(models.Model):
    order_id = models.ForeignKey("order.Orders", on_delete=models.CASCADE, null=True)
    transaxtion_id = models.ForeignKey(Payment, on_delete = models.CASCADE)

    def __str__(self):
        return f"transection {self.id}"
    