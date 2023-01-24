from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from aluno.api.viewsets import AlunoViewSet, AlunoViewSetOut
from disciplina.api.viewsets import DisciplinaViewSet, DisciplinaViewSetOut
from estagio.api.viewsets import EstagioViewSet
from matricula.api.viewsets import MatriculaViewSet, MatriculaViewSetOut
from professor.api.viewsets import ProfessorViewSet

router = routers.DefaultRouter()

router.register(r'listaAluno',AlunoViewSet, basename='ListaAluno')
router.register(r'listaDisciplina',DisciplinaViewSet, basename='ListaDisciplina')
router.register(r'listaEstagio',EstagioViewSet,basename='ListaEstagio')
router.register(r'listaMatricula',MatriculaViewSet,basename='ListaMatricula')
router.register(r'listaProfessor',ProfessorViewSet, basename='ListaProfessor')
router.register(r'viewMatricula',MatriculaViewSetOut,basename='ViewMatricula')
router.register(r'viewAluno',AlunoViewSetOut,basename='ViewAluno')
router.register(r'viewDisciplina',DisciplinaViewSetOut,basename='ViewDisciplina')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
