#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import random

def genera_password():
	'''
	Funcion que implementara una funcion auxiliar recursiva para generar una 
	contrasenia aleatoria.
	Sera de tamanio 10.
	'''
	aux_password(10,'',0)
	
def aux_password(tam,cadena,contador):
	'''
	Funcion recursiva que genera una contrasenia aleatoria segura
	Genera una nueva contrasenia de forma aleatoria tomando en cuenta 
	Numeros, mayusculas, minusculas y caracteres eligiendolos de forma aleatoria.
	'''
	if contador < tam:
		elige= random.randint(0,3)
		if elige == 0:
			cadena= cadena + str(random.randint(0,10))
			#print cadena + ' contador'+ str(contador)+ ' tam '+str(tam)
		elif elige ==1:
			cadena= cadena+ random.choice(['@','#','$','%','&','*','(',')','+', '-', '/'])
			#print cadena + ' contador'+ str(contador)+ ' tam '+str(tam)
		elif elige ==2:
			cadena= cadena +random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
			#print cadena + ' contador'+ str(contador)+ ' tam '+str(tam)
		elif elige ==3:
			cadena= cadena +random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
			#print cadena + ' contador'+ str(contador)+ ' tam '+str(tam)	
		return aux_password(tam,cadena,contador+1)
	else:
		print cadena
	
genera_password()
