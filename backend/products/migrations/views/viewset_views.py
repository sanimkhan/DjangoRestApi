from rest_framework import viewsets

from products.models import Product
from products.permissions import IsCustomer, IsCustomerOrAdmin, IsAdmin
from products.serializers import PrimaryProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PrimaryProductSerializer

    # permission_classes = [permissions.IsAuthenticated]

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

# if want to create only list and post endpoint
# class ProductViewSet(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      viewsets.GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = PrimaryProductSerializer
