from rest_framework.serializers import ModelSerializer
from estacionamento.models import Carro

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id','plate','time','paid','left']