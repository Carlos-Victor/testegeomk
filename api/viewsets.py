from rest_framework import viewsets
from estacionamento.models import Carro
from .serializers import CarroSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer