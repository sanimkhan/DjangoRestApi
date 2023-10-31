import json

from django.http import JsonResponse


def api_home(request):

    try:
        json_data = json.loads(request.body)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    print(json_data)

    return JsonResponse({"message": "Hi, this is django"})
