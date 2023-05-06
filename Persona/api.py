from .models import Persona
from rest_framework import viewsets, permissions
from .serializers import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.AllowAny]