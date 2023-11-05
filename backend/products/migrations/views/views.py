from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import PrimaryProductSerializer


@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    serializer = PrimaryProductSerializer(product)
    return Response(serializer.data)
