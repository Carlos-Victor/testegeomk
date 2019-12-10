from rest_framework import viewsets
from estacionamento.models import Carro
from .serializers import CarroSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime

def change_minutes(queryset):
    for consult in queryset:
        if consult.left == False:
            atual = datetime.strptime(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"), '%Y-%m-%dT%H:%M:%S.%fZ')
            criado = datetime.strptime(str(consult.criado), '%Y-%m-%d %H:%M:%S.%f+00:00')
            minutos = atual - criado
            minutos = int(minutos.seconds/60)
            print(atual)
            print(criado)
            print(consult.criado)
            consult.time = ("%d minutes" % minutos)
            consult.save()



class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def destroy(self, request, pk=None):
        snippet = Carro.objects.filter(plate=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk):
        queryset = Carro.objects.filter(plate=pk)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        change_minutes(queryset)
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
            if carro_out.paid == False:
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
            elif carro_out.paid == True and carro_out.left == False :
                carro_out.left = True
                carro_out.saida = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                carro_out.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_304_NOT_MODIFIED)
                
    
    @action(detail=True, methods=['put'])
    def pay(self, request, pk):
        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            carro_paid = Carro.objects.get(pk=pk)
            if carro_paid.paid == False:
                carro_paid.paid = True
                carro_paid.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_304_NOT_MODIFIED)
