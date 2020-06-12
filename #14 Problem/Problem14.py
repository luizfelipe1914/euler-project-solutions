#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

# Gabarito: 837799, 524 elementos.

number = 1
maior_sequencia = 0
elemento_maior = 0

while(number <= 1000000):

    number_conjecture = number
    contador = 0
    
    while(number_conjecture != 1):
        if(number_conjecture % 2 == 0):
            number_conjecture = (number_conjecture // 2)
        else:
            number_conjecture = (( 3 * number_conjecture) + 1) 
        contador = contador + 1
        
    if(contador > maior_sequencia):
        maior_sequencia = contador
        elemento_maior = number
    number = number + 1

print("O elemento: ", elemento_maior, " gera a maior sequência com ", maior_sequencia, " elementos")