from django.http import JsonResponse
from rest_framework import generics, mixins, status
from products.models import Product
from products.serializers import PrimaryProductSerializer


class ProductMixin(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = PrimaryProductSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request)

    def post(self, request, *args, **kwargs):
        if 'no' in request.data.get('title', '').lower():
            return JsonResponse({"error": "The title cannot contain the word 'no'."},
                                status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.price > 500:
            return JsonResponse({"error": "Cannot delete products with a price greater than 500."},
                                status=status.HTTP_400_BAD_REQUEST)
        return self.destroy(request, *args, **kwargs)
