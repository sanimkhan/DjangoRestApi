from rest_framework import generics
from products.models import Product
from products.serializers import PrimaryProductSerializer


# class ProductDetailView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = PrimaryProductSerializer
#
#
# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = PrimaryProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PrimaryProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = PrimaryProductSerializer
