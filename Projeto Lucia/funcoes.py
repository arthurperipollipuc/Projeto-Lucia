# funções para main3.py
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def somente_int(texto):

    if texto == "":
        return False
    
    numeros_validos = "0123456789"
    
    for char in texto:
        if char not in numeros_validos:
            return False
    
    return True

def somente_float(texto):
    if texto == "":
        return False
    
    
    if texto[0] == '-':
        texto_para_verificar = texto[1:]
    else:
        texto_para_verificar = texto
        
    
    if texto_para_verificar == "" or texto_para_verificar == ".":
        return False
    
    numeros_validos = "0123456789."
    contagem_pontos = 0
    
    for char in texto_para_verificar:
        if char not in numeros_validos:
            return False
        if char == '.':
            contagem_pontos += 1
            

    if contagem_pontos > 1:
        return False
    
    return True