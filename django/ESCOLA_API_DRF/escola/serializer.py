from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #se deixar sem nada trás tudo, mas posso dizer quais fields nao quero tb

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    #melhorando a apresentação. Vou retornar as descrições e nao ids na resposta da chamada rest
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField() #espera uma função get_[nomedocampo] A read-only field that get its representation from calling a method on the parent serializer class. The method called will be of the form "get_{field_name}", and should take a single argument, which is the object being serialized.
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    
    def get_periodo(self, objeto):#chamei de objeto
        return objeto.get_periodo_display() #exibe não "M" mas sim "Matutino" como vemos la na tela de admin e da tela django rest

class ListaAlunosMatriculadosCurso(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']