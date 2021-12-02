from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name

class Measurements(models.Model):
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        verbose_name = 'Показания'
        verbose_name_plural = 'Показания'

    def __str__(self):
        return self.temperature
