#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TRABALHO UNISEP 2017 - CALCULADORA ROMANA 
# Alisson Moretto & Wagner Sariolli

teclas_e_numeros = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'))

def inteiroRomano(i):
    resulta = []
    for inteiro, numeral in teclas_e_numeros:
        conta = int(i / inteiro)
        resulta.append(numeral * conta)
        i -= inteiro * conta
    return ''.join(resulta)

def menu():
    print """ 
              \\||      
             ,'_,-\    | - CALCULADORA ROMANA - |
             ;'____\     
             || =\=|     by: Alisson Moretto
             ||  - |         Wagner Sariolli                        
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\      / , ; [+] ADICAO [-] SUBTRACAO
     /  ,' | _ - ',/, ; [*] MULTIPLICACAO [/] DIVISAO
"""
def romanoInteiro(n):
    n = unicode(n).upper()
    i = resulta = 0
    for inteiro, numeral in teclas_e_numeros:
        while n[i:i + len(numeral)] == numeral:
            resulta += inteiro
            i += len(numeral)
    return resulta

def main():    
    entrada = raw_input('Selecione uma operacao (ex: +,-,*,/): ')
    if entrada.upper() == '+' or entrada.upper() == 'ADICAO':
        numero1 = raw_input('Insira o primeiro numero: ')
        numero2 = raw_input('Insira o segundo numero: ')
        resultaado = romanoInteiro(numero1) + romanoInteiro(numero2)
        print '\n Resultado: ' + inteiroRomano(resultaado) + '\n'
    elif entrada.upper() == '-' or entrada.upper() == 'SUBTRACAO':
        numero1 = raw_input('Insira o primeiro numero: ')
        numero2 = raw_input('Insira o segundo numero: ')
        resultaado = romanoInteiro(numero1) - romanoInteiro(numero2)
        print '\n Resultado: ' + inteiroRomano(resultaado) + '\n'
    elif entrada.upper() == '*' or entrada.upper() == 'MULTIPLICACAO':
        numero1 = raw_input('Insira o primeiro numero: ')
        numero2 = raw_input('Insira o segundo numero: ')
        resultaado = romanoInteiro(numero1) * romanoInteiro(numero2)
        print '\n Resultado: ' + inteiroRomano(resultaado) + '\n'
    elif entrada.upper() == '/' or entrada.upper() == 'DIVISAO':
        numero1 = raw_input('Insira o primeiro numero: ')
        numero2 = raw_input('Insira o segundo numero: ')
        resultaado = romanoInteiro(numero1) / romanoInteiro(numero2)
        print '\n Resultado: ' + inteiroRomano(resultaado) + '\n'
    else:
        print 'Operacao invalida'
menu()    
while True:
    main()
