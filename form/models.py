from django.db import models

class CNAB(models.Model):
    file = models.FileField(upload_to='cnab/')
    processed = models.BooleanField(default=False)

class CNABData(models.Model):
    type = models.IntegerField()
    data = models.CharField(max_length=10)
    value = models.IntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=20)
    hour = models.CharField(max_length=10)
    store_owner = models.CharField(max_length=50)
    store_name = models.CharField(max_length=50)


