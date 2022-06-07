from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    last_name = None
    first_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    address = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, null=True, default="")
    phone_num = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='images/profile_image', blank=True)


