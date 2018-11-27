#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def revisa_palindormo(cadena):	
	'''
	Esta funcion revisa una cadena y regresa el palindromo mas largo
	
	Lo que hara sera comparar uno a uno cada caracter de la cadena
	original con los de la cadena de forma inversa verificando todas
	las combinaciones posibles.
	Si la cadena coincide se guarda la cadena y se vulve a buscar
	otro palindromo para saber si hay una mas larga comparando sus tamanios
	'''
	cad= cadena
	tam_larga=0 #aqui se guarda el tamanio de la mas larga
	cad_larga='' #aqui se guarda la cadena mas larga
	for i in range(0,len(cadena)):
		for j in range(0,len(cadena)):
			#print 'origina: '+cadena[i:j+1:] +'\nreversa: '+ cadena[j:i-1:-1] 
			if cadena[i:j:]== cadena[j:i:-1] and (j-i) > tam_larga: #verificamos si es palindromo y los tamanios
				cad_larga = cadena[i:j+1:]
				tam_larga = len(cadena[i:j:]) 
			else:
				continue
	return cad_larga
	
	
def es_primo(num):
	'''
	Funcion que recibe un numero y verifica si este es primo o no
	Primero descarta los prrimero numeros que no cumplen las reglas
	de dividirse nicamente entr si mismo y 1.
	Despues verifica para el resto que no sea divisible entre
	otros que no sean el mismo y 1.
	'''
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				
				return False
		return True


def n_primos(n):
	'''
	Funcion que devuelve los n primeros numeros primos mediante
	la llamada a una funcion recursiva.
	'''
	return aux_n_primos(n,1,[2],3)
	
def aux_n_primos(n,contador,lista,ultimo):
	'''
	Funcion que devuelve una lista de n numeros primos donde:
	n= La cantidad de los primeros numeros primos
	contador= Un auxiliar para contar los n numeros
	lista= Es el conjunto de los numeros primos calculados actualmente
	ultimo= sera el ultimo numero primo calculado
	'''
	if contador <= n:
		if es_primo(ultimo):
			lista.append(ultimo)
			return aux_n_primos(n, contador+1, lista, ultimo+1)
		else:
			return aux_n_primos(n, contador, lista, ultimo+1)
	else:
		return lista 
	
	
	
	
	
print revisa_palindormo('ASDanitalavalatinasacvbgososo')
print es_primo(25)
print n_primos(15)
