#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

number = 1
soma_pares = 0
qtd_pares = 0

while(number <  10000):
    index = 1
    soma = 0
    while(index < number):
        if(number % index == 0):
            soma = soma + index
        index = index + 1

    if(soma != number):
        soma_div = 0
        index = 1
        while(index < soma):
            if(soma % index == 0):
                soma_div = soma_div + index
            index = index + 1
            
    if(soma_div == number):
        qtd_pares = qtd_pares + 1
        soma_pares = soma_pares + number 
        print("%dº par amigável < 10000: %d e %d \n " %(qtd_pares, number, soma))
    
    number = number + 1
    
print(" \n A soma de todos os pares amigáveis inferiores a 10000 é: ", soma_pares)
print(" \n Quantidade de pares amigáveis no intervalo: ", (qtd_pares // 2))
