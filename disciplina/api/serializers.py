from rest_framework import serializers
from disciplina import models

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = '__all__'

class DisciplinaSerializerNameHoras(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome','carga_horaria']

class DisciplinaSerializerName(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome']
