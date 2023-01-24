from rest_framework import serializers
from aluno import models

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = '__all__'


class AlunoSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = ['nome']