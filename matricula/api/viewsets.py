from rest_framework import viewsets
from matricula import models
from matricula.api import serializers


class MatriculaViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializer
    queryset = models.Matricula.objects.all()

class MatriculaViewSetNomeNpaDisciplina(viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializerNomeNpaDisciplina
    queryset = models.Matricula.objects.all()

