from django.db import models

# Create your models here.

class TempData(models.Model):
    time = models.TimeField()
    tmp = models.DecimalField(max_digits=4, decimal_places=2)

