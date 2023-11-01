import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict


# from products.models import Product


def api_home(request):

    product = Product.objects.all().order_by("?").first()
    data = model_to_dict(product)
    # data = model_to_dict(product, fields= ['id'])

    return JsonResponse(data)
