from rest_framework import serializers
from aluno import models
from disciplina.api.serializers import DisciplinaSerializerName
from estagio.api.serializers import EstagioSerializer


class AlunoSerializer(serializers.ModelSerializer):
    estagio_id = EstagioSerializer();

    class Meta:
        model = models.Aluno
        fields = '__all__'

class AlunoSerializerName(serializers.ModelSerializer):
    # estagio_id = EstagioSerializer();

    class Meta:
        model = models.Aluno
        fields = ['nome']

