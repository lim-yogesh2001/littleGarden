from django.contrib import admin
from .models import AboutUs, PrivacyPolicy, ShippingPolicy

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(PrivacyPolicy)
admin.site.register(ShippingPolicy)
