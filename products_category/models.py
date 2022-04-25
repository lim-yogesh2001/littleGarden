from distutils.command.upload import upload
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="images")
    description = models.TextField()
    price = models.IntegerField(default=0)
    is_recently_added = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

class ProductReview(models.Model):
    ratings = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"



