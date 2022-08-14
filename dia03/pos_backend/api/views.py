from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,Categoria
)

from .serializers import (
    MesaSerializers,CategoriaSerializers
)

class IndexView(APIView):
    def get(self, request):
        context = {
            'ok':True,
            'content':'POS API activo'
        }
        return Response(context)

class MesaView(APIView):
    def get(self,request):
        data = Mesa.objects.all()
        print(data)
        print(type(data))
        serializersData = MesaSerializers(data,many=True)
        context = {
            'ok':True,
            'content':serializersData.data
        }
        print(serializersData)
        print(type(serializersData))
        print(serializersData.data)
        print(type(serializersData.data))
        return Response(context)

class CategoriaView(APIView):
    def get(self,request):
        data = Categoria.objects.all()
        serializersData = CategoriaSerializers(data,many=True)
        context = {
            'ok':True,
            'content':serializersData.data
        }

        return Response(context)