from rest_framework import viewsets
from api.models import Persona,TipoPersona
from api.serializers import PersonaSerializer,TipoPersonaSerializer

class TipoPersonaViewSet (viewsets.ModelViewSet):
    serializer_class = TipoPersonaSerializer
    queryset = TipoPersona.objects.all()
   
class PersonaViewSet (viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
