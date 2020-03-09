#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

seguinte = 0
anterior = 0
soma = 0

while(seguinte < 4000000):
    seguinte = seguinte + anterior
    anterior = seguinte - anterior
    
    if(seguinte == 0):
        seguinte = seguinte + 1
        
    if(seguinte % 2 == 0):
        soma = soma + seguinte
        

print("A soma dos elementos pares menores que 4.000.000 da sequência de Fibonacci é: ", soma)
