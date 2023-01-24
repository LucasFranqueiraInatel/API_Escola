from uuid import uuid1

from django.db import models

from estagio.models import Estagio


class Aluno(models.Model):
    ra = models.IntegerField(primary_key=True, editable=True);
    nome = models.CharField(max_length=45);
    ano_nascimento = models.IntegerField(blank=False, null=False)
    cpf = models.CharField(max_length=14);
    cidade = models.CharField(max_length=45);
    bairro = models.CharField(max_length=45);
    numero = models.IntegerField(blank=False, null=False);
    complemento = models.CharField(max_length=200);
    estagio_id = models.ForeignKey(Estagio, on_delete=models.CASCADE, blank=True, null=True)

