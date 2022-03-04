import re
from validate_docbr import CPF #https://alvarofpp.github.io/validate-docbr/  valida cnh, titulo eleitor, etc

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)
    
    #return len(numero_cpf) == 11 #vai retornar true ou false

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular)
    return resposta