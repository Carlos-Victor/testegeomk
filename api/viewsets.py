from rest_framework import viewsets
from estacionamento.models import Carro
from .serializers import CarroSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def retrieve(self, request, pk):
        queryset = Carro.objects.filter(plate=pk)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for consult in queryset:
            if consult.left == False:
                atual = datetime.strptime(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"), '%Y-%m-%dT%H:%M:%S.%fZ')
                criado = datetime.strptime(str(consult.criado).replace('+00:00', 'Z'), '%Y-%m-%d %H:%M:%S.%fZ')
                minutos = atual - criado
                minutos = int(minutos.seconds/60)
                consult.time = ("%d minutes" % minutos)
                consult.save()
        carro = CarroSerializer(queryset, many=True)
        return Response(carro.data)

    @action(detail=True, methods=['put'])
    def out(self, request, pk):
        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            carro_out = Carro.objects.get(pk=pk)
            if carro_out.paid == True and carro_out.left == False :
                carro_out.left = True
                carro_out.saida = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                carro_out.save()
        return Response({"message":"Pagamento deve ser realizado antes de sair"},status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True, methods=['put'])
    def pay(self, request, pk):
        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            carro_paid = Carro.objects.get(pk=pk)
            carro_paid.paid = True
            carro_paid.save()
            return Response(status=status.HTTP_200_OK)