from rest_framework import serializers

from .models import (
    Mesa, Categoria,Plato,Pedido,PedidoPlato
)

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MesaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class PlatoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plato_img'] = instance.plato_img.url
        return representation

class CategoriaPlatosSerializers(serializers.ModelSerializer):
    Platos = PlatoSerializers(many=True,read_only=True)

    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nom','Platos']

class PedidoPlatoSerializersPOST(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['plato_id','pedidoplato_cant']

class PedidoSerializerPOST(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializersPOST(many=True)

    class Meta:
        model = Pedido
        fields = ['pedido_fecha','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']

    def create(self,validated_data):
        pedidos_data = validated_data.pop('pedidoplatos')
        pedido = Pedido.objects.create(**validated_data)
        for pedido_data in pedidos_data:
            PedidoPlato.objects.create(pedido_id = pedido,**pedido_data)
        return pedido
        