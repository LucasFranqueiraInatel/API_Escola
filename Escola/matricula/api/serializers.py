from rest_framework import serializers
from aluno.api.serializers import AlunoSerializer, AlunoSerializerName
from disciplina.api.serializers import DisciplinaSerializer, DisciplinaSerializerName
from matricula import models


class MatriculaSerializer(serializers.ModelSerializer):
    alunos_ra = AlunoSerializer()
    disciplina_id = DisciplinaSerializer()
    class Meta:
        model = models.Matricula
        fields = '__all__'

class MatriculaSerializerNomeNpaDisciplina(serializers.ModelSerializer):
    alunos_ra = AlunoSerializerName()
    disciplina_id = DisciplinaSerializerName()
    class Meta:
        model = models.Matricula
        fields = ['npa','alunos_ra','disciplina_id']