from django.contrib import admin
from .models import Categories, Product, ProductReview

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_image',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_image', 'category_id', 'is_recently_added', 'is_popular',)
class ProductReviewAdmin(admin.ModelAdmin):
    list_filter = ('ratings',)
    list_display = ('id', 'ratings', 'comment', 'product_id', 'user_id',)

# Register your models here.
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)