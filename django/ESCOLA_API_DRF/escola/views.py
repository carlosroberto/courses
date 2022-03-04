from django.db.models import query
from rest_framework import generics, serializers, viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from escola import serializer # importando viewsets que é class based views
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosCurso
from rest_framework.authentication import BasicAuthentication #autenticação user e pass
from rest_framework.permissions import IsAuthenticated #confere se está autenticado contra os usuarios registrados no django admin


class AlunosViewSet(viewsets.ModelViewSet):
    """ lista todos os alunos """
    queryset = Aluno.objects.all() #tras todos os alunos da base
    serializer_class = AlunoSerializer #determina a classe responsavel por serializar os dados obtidos do model
    #essa classe permite nao precisar definir se é update, delete, etc, 
    # isso se me lembro bem é inerente de class based views que simplificam tasks basicas repetitivas
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    

class CursosViewSet(viewsets.ModelViewSet):
    """ lista todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listar matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']) #a ideia é capturar o id do aluno (aluno_id é o objeto aluno e seu id na notação do django) e vai ser usado na url aluno/{id}/matriculas
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """listar alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCurso
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]