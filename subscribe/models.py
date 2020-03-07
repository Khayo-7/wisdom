from django.db import models

# Create your models here.
from django.db import models

class subscribe(models.Model):   
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length = 60)
    status = models.CharField(max_length = 60)
    body = models.TextField()
    created_at = models.DateTimeField('created_at')


class vehicle(models.Model):
    plate_no = models.CharField('plate Number', max_length=20)
    vehicle_code = models.CharField('vehicle code', max_length=20)
    vehicle_model = models.CharField(max_length=30)
    owner = models.CharField(max_length = 60)
    status = models.CharField(max_length = 60)
    created_at = models.DateTimeField('created_at')