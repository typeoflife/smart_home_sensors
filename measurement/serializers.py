from rest_framework import serializers

from measurement.models import Measurements, Sensor



class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurements
        fields = ['temperature', 'created_at', 'sensor']


class SensorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
