from rest_framework import serializers

from disciplina.api.serializers import DisciplinaSerializer, DisciplinaSerializerNameHoras
from professor import models

class ProfessorSerializer(serializers.ModelSerializer):
    disciplina_id = DisciplinaSerializerNameHoras()

    class Meta:
        model = models.Professor
        fields = '__all__'