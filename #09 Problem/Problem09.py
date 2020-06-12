#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

# Gabarito: 31875000

a = 1
while(a <= 998):
    b = a + 1
    while(b <= 998):
        c = 1000 - a -b
        if((a**2) + (b**2) == (c**2)):
            print(a * b * c)
        b = b + 1
    a = a +1