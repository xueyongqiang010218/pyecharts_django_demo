from django.db import models

class company(models.Model):
    name = models.CharField(max_length=50)
    shu = models.IntegerField(max_length=50)

