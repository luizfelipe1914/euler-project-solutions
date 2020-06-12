#!/usr/bin/env python3
#-*- encoding:UTF-8 -*-

import fractions

resposta = 1
index = 1
while(index < 21):
    resposta = resposta * index // fractions.gcd(resposta, index)
    index = index + 1

print(resposta)