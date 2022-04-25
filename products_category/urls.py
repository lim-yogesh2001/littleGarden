from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryView.as_view(), name="category-list"),
    path("categories/products/<int:category_id>/", views.CategoryProductView.as_view(), name="category-products"),
    path("products/", views.ProductsView.as_view(), name="products-list"), # products that are is not popular and is not recently added 
    path("products/recently/", views.RecentlyAddedProducts.as_view(), name="recently-products"),
    path("products/popular/", views.PopularProducts.as_view(), name="popular-products"),
    path("products/<int:id>/", views.ProductDetail.as_view(), name="product-detail"),
    path("products/reviews/<int:product_id>", views.ProductReviews.as_view(), name="product-reviews"),
    path("products/reviews/", views.ProductALLReview.as_view(), name="product-reviews-list"),
    path("products/review-details/<int:id>", views.ProductReviewDetail.as_view(), name="product-review-details")
]
