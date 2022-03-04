from django.contrib import admin
from escola import models
from escola.models import Aluno, Curso, Matricula
# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento') #campos que vao aparecer na tela de admin 
    list_display_links = ('id','nome')  #campos que podem ser clicados para detalhes
    search_fields = ('nomes',) #criar searchbar buscar por nomes
    list_per_page = 20 #paginação

admin.site.register(Aluno,Alunos) #passando o Aluno que importei la em em cima e a nova classe Alunos acima.

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao') #campos que vao aparecer na tela de admin 
    list_display_links = ('id','codigo_curso')  #campos que podem ser clicados para detalhes
    search_fields = ('codigo_curso',) #criar searchbar buscar por nomes
    list_per_page = 20 #paginação

admin.site.register(Curso,Cursos) #passando o Aluno que importei la em em cima e a nova classe Alunos acima.

class Matriculas(admin.ModelAdmin):
    list_display = ('id','aluno','curso', 'periodo') #campos que vao aparecer na tela de admin 
    list_display_links = ('id',)  #campos que podem ser clicados para detalhes

admin.site.register(Matricula,Matriculas) #passando o Aluno que importei la em em cima e a nova classe Alunos acima.
