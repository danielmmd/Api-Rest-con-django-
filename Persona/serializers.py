from rest_framework import serializers

from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'apellido', 'edad', 'telefono', 'email', 'direccion', 'created', 'updated')
        read_only_fields = ('created', 'updated')
        