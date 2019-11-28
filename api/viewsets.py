from rest_framework import viewsets
from estacionamento.models import Carro
from .serializers import CarroSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    # def retrieve(self, request, pk=None, str):
    #     queryset = Carro.objects.all().filter(plate=str)
    #     carro = get_object_or_404(queryset, plate=str)
    #     carro = CarroSerializer(carro, many=True)
    #     return Response(carro.data)
        #     def retrieve(self, request, pk=None):
        # queryset = User.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        # serializer = UserSerializer(user)
        # return Response(serializer.data)
        # try:
        #    carro = Carro.objects.all().filter(plate=plate)
        #    serializer = CarroSerializer(carro, many=True)
        # except Carro.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def out(self, request, pk):
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

    @action(detail=True, methods=['post'])
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