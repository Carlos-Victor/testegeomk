from rest_framework import viewsets
from estacionamento.models import Carro
from .serializers import CarroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    @api_view(['GET'])
    def historico(request,plate):
        try:
           carro = Carro.objects.all().filter(plate=plate)
           serializer = CarroSerializer(carro, many=True)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)


    @api_view(['PUT'])
    def carro_put_saida(request, pk):
        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            carro_out = Carro.objects.get(pk=pk)
            if carro_out.paid == True:
                carro_out.left = True
                carro_out.save()
                return Response(status=status.HTTP_200_OK)
        return Response({"message":"Pagamento deve ser realizado antes de sair"},status=status.HTTP_401_UNAUTHORIZED)

    @api_view(['PUT'])
    def carro_put_pagamento(request, pk):
        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            carro_paid = Carro.objects.get(pk=pk)
            carro_paid.paid = True
            carro_paid.save()
            return Response(status=status.HTTP_200_OK)