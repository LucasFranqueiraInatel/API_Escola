from django.db import models
from aluno.models import Aluno
from disciplina.models import Disciplina

class Matricula(models.Model):
    np1 = models.IntegerField()
    np2 = models.IntegerField()
    np3 = models.IntegerField()
    npa = models.IntegerField()
    alunos_ra = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)