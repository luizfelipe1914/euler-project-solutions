#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

# Gabarito: 10001º = 104743

from math import sqrt

number = 2
cont = 0
while(cont < 10001):
    index = 2
    contador = 0
    while(index <= sqrt(number)):
        if(number % index == 0):
            contador = contador + 1
        index = index + 1
    if(contador == 0):
        cont = cont + 1
        if(cont == 10001):
            print("%dº = %d" %(cont, number))
    number = number +1