#!/usr/bin/env python3
#-*- encoding:UTF-8 -*-

number = 1
soma = 0
while(number < 1000):
    if(number % 3 == 0 or number % 5 == 0):
        soma = soma + number
    number = number + 1

print("A soma dos múltiplos de 3 ou 5 no intervalo [1, 1000[ é:", soma)
