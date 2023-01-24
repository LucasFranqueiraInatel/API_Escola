from uuid import uuid1

from django.db import models

from aluno.models import Aluno
from disciplina.models import Disciplina


class Matricula(models.Model):
    aluno_ra = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True);
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True);
    np1 = models.IntegerField(blank=False, null=False);
    np2 = models.IntegerField(blank=False, null=False);
    np3 = models.IntegerField(blank=False, null=False);
    npa = models.IntegerField(blank=False, null=False);
    id = models.IntegerField(primary_key=True, editable=True);

