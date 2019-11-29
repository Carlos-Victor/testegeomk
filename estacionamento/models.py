from django.db import models
from .validators import placa
from datetime import datetime
# Create your models here.
class Carro(models.Model):
    time = models.CharField("Minutos", max_length=12, default='0 minutos')
    criado = models.DateTimeField("Criado",default=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
    paid = models.BooleanField("Pagamento", default=False)
    saida = models.DateTimeField("Saida", default='2019-01-01T00:00:00.000000Z')
    left = models.BooleanField("Canhoto", default=False)
    plate = models.CharField("Placa", max_length=8, validators=[placa]) 