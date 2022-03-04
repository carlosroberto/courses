from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF invalido'}) #tenho de mandar um dicionario com o nome do campo para que haja uma identificação de qual campo causou o problema)
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não incluir números no nome'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"RG tem de ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"Celular deve ser no formato XX XXXXX-XXXX"})

        return data



    # essa é uma forma de fazer validação direta aqui, a outra é usando o arquivo validators.py
    # def validate_cpf(self,cpf):
    #     if len(cpf)!= 11:
    #         raise serializers.ValidationError("CPF tem de ter 11 dígitos")
    #     return cpf

    # def validate_nome(self,nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não incluir números no nome")
    #     return nome

    # def validate_rg(self,rg):
    #     if len(rg)!= 9:
    #         raise serializers.ValidationError("RG tem de ter 9 dígitos")
    #     return rg   

    # def validate_celular(self,celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("Celular tem de ter 11 dígitos")
    #     return celular   