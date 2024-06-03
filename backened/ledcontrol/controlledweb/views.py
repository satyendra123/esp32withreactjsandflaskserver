# views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import requests

led_status = "off"

@api_view(['POST'])
def led_on_view(request):
    global led_status
    try:
        led_status = "on"
        return JsonResponse({'status': 'success', 'message': 'LED is turned on'}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'status': 'Failed to turn on LED', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def led_off_view(request):
    global led_status
    try:
        led_status = "off"
        return JsonResponse({'status': 'success', 'message': 'LED is turned off'}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'status': 'Failed to turn off LED', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def led_status_view(request):
    global led_status
    return JsonResponse({'status': led_status}, status=status.HTTP_200_OK)
