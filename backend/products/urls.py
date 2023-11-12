from django.urls import path

from products.migrations.views.generic_views import ProductDetail, ProductList
from products.migrations.views.views import product_detail

urlpatterns = [
    path('<int:pk>', product_detail),
    path('generics/<int:pk>/', ProductDetail.as_view()),
    path('generics/', ProductList.as_view()),
]
