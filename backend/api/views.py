from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import PrimaryProductSerializer


# JsonResponse is not suggested, it does not have CSF configured
# Better use rest_framework

def api_general_response(request):
    product = Product.objects.all().order_by("?").first()
    data = model_to_dict(product)
    # data = model_to_dict(product, fields= ['id'])

    return JsonResponse(data)


@api_view(['GET', 'POST'])
def api_django_response_get(request):
    if request.method == 'GET':
        product = Product.objects.all().order_by("?").first()
        data = PrimaryProductSerializer(product).data

        return Response(data)
    elif request.method == 'POST':
        serializer = PrimaryProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# @api_view(["POST"])
# def api_django_response_post(request):
#     serializer = PrimaryProductSerializer(data=request.body)
#     if serializer.is_valid():
#         print(serializer.data)
#
#     return Response(serializer.data)
