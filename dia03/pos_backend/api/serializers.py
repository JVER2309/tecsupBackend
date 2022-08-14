from rest_framework import serializers

from .models import (
    Mesa, Categoria,Plato
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