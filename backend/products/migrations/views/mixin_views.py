from django.http import JsonResponse
from rest_framework import generics, mixins, status

from products.models import Product
from products.permissions import IsCustomer, IsAdmin, IsCustomerOrAdmin
from products.serializers import PrimaryProductSerializer


class ProductMixin(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Product.objects.all()
    # queryset = Product.objects.all().order_by('-id')
    serializer_class = PrimaryProductSerializer

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'GET':
            if 'pk' in self.kwargs:
                self.permission_classes = [IsCustomer]
            else:
                self.permission_classes = [IsCustomerOrAdmin]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAdmin]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAdmin]
        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            sort_by = request.GET.get('sort', 'id')  # Default to sorting by ID ascending
            self.queryset = self.queryset.order_by(sort_by)
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
