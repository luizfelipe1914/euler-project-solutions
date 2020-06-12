#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

# Gabarito: 25164150

i = 1
soma_quad = 0
quad_soma = 0

while(i < 101):
    soma_quad = soma_quad + (i ** 2)
    quad_soma = quad_soma + i
    i = i + 1
    
quad_soma = quad_soma ** 2

print(quad_soma - soma_quad)