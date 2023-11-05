from rest_framework import generics
from products.models import Product
from products.serializers import PrimaryProductSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = PrimaryProductSerializer


class BookListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = PrimaryProductSerializer
