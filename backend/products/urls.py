from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.migrations.views.generic_views import ProductDetail, ProductList
from products.migrations.views.mixin_views import ProductMixin
from products.migrations.views.views import product_detail
from products.migrations.views.viewset_views import ProductViewSet

router = DefaultRouter()
router.register(r'viewsets', ProductViewSet)

urlpatterns = [
    path('<int:pk>', product_detail),

    path('', include(router.urls)),

    path('generics/<int:pk>/', ProductDetail.as_view()),
    path('generics/', ProductList.as_view()),

    path('mixins/', ProductMixin.as_view()),
    path('mixins/<int:pk>/', ProductMixin.as_view()),

    path('product/', ProductDetail.as_view(), name="list-create"),
]
