from django.urls import path

from measurement.views import SensorsView, CurrentSensorView, MeasurementCreateView


urlpatterns = [
    path('sensors/', SensorsView.as_view(), name='sensors_list'),
    path('sensors/<pk>/', CurrentSensorView.as_view(), name='current_sensor'),
    path('measurement/', MeasurementCreateView.as_view(), name='measurementcreate')
]