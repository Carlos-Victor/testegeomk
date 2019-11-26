from django.db import models
from .validators import placa
# Create your models here.
class Carro(models.Model):
    time = models.DurationField("Minutos")
    criado = models.TimeField("Criado",auto_now_add=True)
    paid = models.BooleanField("Pagamento", default=False)
    left = models.BooleanField("Canhoto", default=False)
    plate = models.CharField("Placa", max_length=8, validators=[placa])