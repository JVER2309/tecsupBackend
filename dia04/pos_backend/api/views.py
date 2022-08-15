from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,
    Categoria,
    Plato,
    Pedido
)

from .serializers import (
    CategoriaPlatosSerializers, 
    MesaSerializers,
    CategoriaSerializers,
    PlatoSerializers,
    PedidoSerializerPOST
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

class PlatoView(APIView):
    def get(self,request):
        data = Plato.objects.all()
        serializersData = PlatoSerializers(data,many=True)
        context = {
            'ok':True,
            'content':serializersData.data
        }

        return Response(context)

class CategoriaDetailView(APIView):
    def get(self, request, categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serializersData = CategoriaSerializers(data)
        context = {
            'ok':True,
            'content':serializersData.data
        }

        return Response(context)

class CategoriaPlatosView(APIView):
    def get(self, request, categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serializersData = CategoriaPlatosSerializers(data)
        context = {
            'ok':True,
            'content':serializersData.data
        }

        return Response(context)

class PedidoView(APIView):
    def post(self,request):
        serializersData = PedidoSerializerPOST(data=request.data)
        serializersData.is_valid(raise_exception=True)
        serializersData.save()

        context = {
            'ok':True,
            'content':serializersData.data
        }

        return Response(context)