'''
from django.urls import path
from .views import led_on_view, led_off_view

urlpatterns = [
    path('led/on/', led_on_view, name='led_on_view'),
     path('led/off/', led_off_view, name='led_off_view'),
]
'''
# myapp/urls.py

from django.urls import path
from .views import led_on_view, led_off_view, led_status_view

urlpatterns = [
    path('api/led/on/', led_on_view, name='led_on'),
    path('api/led/off/', led_off_view, name='led_off'),
    path('api/led/status/', led_status_view, name='led_status'),
]
