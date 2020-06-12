#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

from math import sqrt

NUMBER = 600851475143
index = 2
maior = 0
while(index < NUMBER):
    num = 1
    while(num < NUMBER // 2):
        i = 2
        contador = 0
        while(i < sqrt(num)):
            if(num % i):
                contador = contador + 1
            i = i + 1
        if(contador == 0):
            if(NUMBER % num == 0):
                if(num > maior):
                    maior = num
        num = num + 1
    index = index + 1

print(maior)