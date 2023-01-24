
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from aluno.api.viewsets import AlunoViewSet
from disciplina.api.viewsets import DisciplinaViewSet, DisciplinaViewSetNameHoras
from estagio.api.viewsets import EstagioViewSet
from matricula.api.viewsets import MatriculaViewSet, MatriculaViewSetNomeNpaDisciplina
from professor.api.viewsets import ProfessorViewSet

router = routers.DefaultRouter()
router.register(r'listaAluno',AlunoViewSet, basename='ListaAluno')
router.register(r'listaEstagio',EstagioViewSet, basename='ListaEstagio')
router.register(r'listaDisciplina',DisciplinaViewSet, basename='ListaDisciplina')
router.register(r'listaProfessor',ProfessorViewSet, basename='ListaProfessor')
router.register(r'listaMatricula',MatriculaViewSet, basename='ListaMatricula')
# router.register(r'nomeHorasDisciplina',DisciplinaViewSetNameHoras)
router.register(r'nomeNpaDisciplina',MatriculaViewSetNomeNpaDisciplina,basename='ViewMatricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
