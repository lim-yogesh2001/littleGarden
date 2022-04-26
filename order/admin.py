from django.contrib import admin
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'date', 'quantity', 'status', 'shipping_time')
# Register your models here.
admin.site.register(Orders, OrdersAdmin)
