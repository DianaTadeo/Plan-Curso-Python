#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#XML - parser

import random
lista = ['diana','jesi', 'pedro']
print {nom: random.randint(0,10) for nom in lista}

#diccionario de numeros odiosos
print {n: (bin(n),hex(n)) for n in range(0,50) if str(bin(n)).count('1') %2!=0 }
