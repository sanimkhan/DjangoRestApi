from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from django.forms.models import model_to_dict


def api_general_response(request):
    product = Product.objects.all().order_by("?").first()
    data = model_to_dict(product)
    # data = model_to_dict(product, fields= ['id'])

    return JsonResponse(data)


@api_view(["GET"])
def api_django_response(request):
    product = Product.objects.all().order_by("?").first()
    data = model_to_dict(product)
    # data = model_to_dict(product, fields= ['id'])

    return Response(data)
