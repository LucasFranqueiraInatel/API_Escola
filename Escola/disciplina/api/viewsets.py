from rest_framework import viewsets
from disciplina import models
from disciplina.api import serializers


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializer

class DisciplinaViewSetNameHoras(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializerNameHoras

class DisciplinaViewSetName(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializerNameHoras
