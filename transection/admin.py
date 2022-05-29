from django.contrib import admin
from .models import Payment, Transection

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type')

class TransectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'transaxtion_id',)

# Register your models here.
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Transection, TransectionAdmin)