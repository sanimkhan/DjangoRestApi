from django.urls import path

from products.migrations.views.generic_views import ProductDetail, ProductList
from products.migrations.views.mixin_views import ProductMixin
from products.migrations.views.views import product_detail

urlpatterns = [
    path('<int:pk>', product_detail),

    path('generics/<int:pk>/', ProductDetail.as_view()),
    path('generics/', ProductList.as_view()),

    path('mixins/', ProductMixin.as_view()),
    path('mixins/<int:pk>/', ProductMixin.as_view()),
]
