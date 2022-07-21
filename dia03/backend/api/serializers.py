from rest_framework import serializers

# Importamos el modelo User
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        # Argumentos extra para nuestro modelo -> ocultamos el password
        extra_kwargs = {'password':{'write_only':True}}


    # Validated_data recibe la toda la data
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )
        # Encriptar el password
        user.set_password(validated_data['password'])
        user.save()
        return user