#!/usr/bin/python
# -*- coding: utf-8 -*-

#SOLO SIRVE PARA ARCHIVOS CON 3 PALABRAS
'''
AVISO IMPORTANTE: Es posible que la ejecucion tarde, sin embargo trabajare
en eso en un futuro.

ejecucion ej:
			python passwd_generator.py claves.txt
			
Se creara el archivo llamado 'generadas.txt' donde se guardan los passwords generados
'''
import sys

#Es posible agregar m[as caracteres a cada lista de acuerdo al criterio
lista_a= ['4','@', '9']
lista_b= ['8','3','6']
lista_c= ['<','0','(']
lista_g= ['9','6']
lista_i= ['1','!','|','/','[',']','(',')']
lista_j= ['!','/']
lista_l= ['1','!','/','|','[',']','(',')']
lista_n= ['7','^']
lista_o= ['0','@','*','.']
lista_p= ['?','>']
lista_s= ['5','$']
lista_t= ['+','7']
lista_y= ['&','!']
lista_z= ['7','/']
abcdario=['a','c','g','i','j','l','n','o','p','s','t','y','z']

def crea_generacion(lista):
	'''
	Funcion que crea una nueva generacion de passwords a partir de una
	lista de passwords.
	Cada generacion es calculada de acuerdo al intercambio de letras por
	caracteres
	'''
	generacion=[]
	for palabra in lista:
		for letra in abcdario:
			nueva=convertLetra(palabra,letra)
			lista=nueva
			if nueva: 
				generacion= generacion+nueva
	return list(set(generacion))
				
			
def convertLetra(palabra,letra):
	'''
	Funcion que intercambia las letras que encuentre por algun caracter 
	de la lista de caracteres que le corresponde.
	Regresa una lista con todas las posibles palabras con diferentes
	caracteres que se cambian por una letra
	'''
	lista_palabras=[]
	if (('a' in palabra)| ('A' in palabra)) and letra=='a':
		for char in lista_a:
			nueva=palabra
			if 'a' in palabra:
				nueva=palabra.replace('a',char)
			if 'A' in palabra:
				nueva=nueva.replace('A',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('b' in palabra) | ('B' in palabra)) and letra=='b':
		for char in lista_b:
			nueva=palabra
			if 'b' in palabra:
				nueva=palabra.replace('b',char)
			if 'B' in palabra:
				nueva=nueva.replace('B',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('c' in palabra) | ('C' in palabra)) and letra=='c':
		for char in lista_c:
			nueva=palabra
			if 'c' in palabra:
				nueva=palabra.replace('c',char)
			if 'C' in palabra:
				nueva=nueva.replace('C',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('e' in palabra) | ('E' in palabra)) and letra=='e':
		if 'e' in palabra:
			palabra=palabra.replace('e','3')
		if 'E' in palabra:
			palabra=palabra.replace('E','3')
		lista_palabras.append(palabra)
	elif (('g' in palabra) | ('G' in palabra)) and letra=='g':
		for char in lista_g:
			nueva=palabra
			if 'g' in palabra:
				nueva=palabra.replace('g',char)
			if 'G' in palabra:
				nueva=nueva.replace('G',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('i' in palabra) | ('I' in palabra)) and letra=='i':
		for char in lista_i:
			nueva=palabra
			if 'i' in palabra:
				nueva=palabra.replace('i',char)
			if 'I' in palabra:
				nueva=nueva.replace('I',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('l' in palabra) | ('L' in palabra)) and letra=='l':
		for char in lista_l:
			nueva=palabra
			if 'l' in palabra:
				nueva=palabra.replace('l',char)
			if 'L' in palabra:
				nueva=nueva.replace('L',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('n' in palabra) | ('N' in palabra)) and letra=='n':
		for char in lista_n:
			nueva=palabra
			if 'n' in palabra:
				nueva=palabra.replace('n',char)
			if 'N' in palabra:
				nueva=nueva.replace('N',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('o' in palabra) | ('O' in palabra)) and letra=='o':
		for char in lista_o:
			nueva=palabra
			if 'o' in palabra:
				nueva=palabra.replace('o',char)
			if 'O' in palabra:
				nueva=nueva.replace('O',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('p' in palabra) | ('P' in palabra)) and letra=='p':
		for char in lista_p:
			nueva=palabra
			if 'p' in palabra:
				nueva=palabra.replace('p',char)
			if 'P' in palabra:
				nueva=nueva.replace('P',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('s' in palabra) | ('S' in palabra)) and letra=='s':
		for char in lista_s:
			nueva=palabra
			if 's' in palabra:
				nueva=palabra.replace('s',char)
			if 'S' in palabra:
				nueva=nueva.replace('S',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('t' in palabra) | ('T' in palabra)) and letra=='t':
		for char in lista_t:
			nueva=palabra
			if 't' in palabra:
				nueva=palabra.replace('t',char)
			if 'T' in palabra:
				nueva=nueva.replace('T',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('y' in palabra) | ('Y' in palabra)) and letra=='y':
		for char in lista_y:
			nueva=palabra
			if 'y' in palabra:
				nueva=palabra.replace('y',char)
			if 'Y' in palabra:
				nueva=nueva.replace('Y',char)
			lista_palabras.append(nueva)
		palabra=nueva
	elif (('z' in palabra) | ('Z' in palabra)) and letra=='a':
		for char in lista_z:
			nueva=palabra
			if 'z' in palabra:
				nueva=palabra.replace('z',char)
			if 'Z' in palabra:
				nueva=nueva.replace('Z',char)
			lista_palabras.append(nueva)
		palabra=nueva
	else:
		return 
	return lista_palabras
			
def combinaciones(palabra1,palabra2,palabra3):
	'''
	Calcula las posibles combinaciones en segmentos de las palabras que se le pasen
	'''
	resultado=[]
	for i in range(0,len(palabra1)):
		for j in range(0,len(palabra2)):
			for k in range(0,len(palabra3)):
				resultado.append(palabra1[i::].lower()+palabra2[j::].lower()+palabra3[k::].lower())
				resultado.append(palabra1[i::].lower()+palabra2[j::].lower()+palabra3[:k:].lower())
				resultado.append(palabra1[:i:].lower()+palabra2[:j:].lower()+palabra3[k::].lower())
				resultado.append(palabra1[:i:].lower()+palabra2[:j:].lower()+palabra3[:k:].lower())
				resultado.append(palabra1[i::].upper()+palabra2[j::].upper()+palabra3[k::].upper())
				resultado.append(palabra1[i::].upper()+palabra2[j::].upper()+palabra3[:k:].upper())
				resultado.append(palabra1[:i:].upper()+palabra2[:j:].upper()+palabra3[k::].upper())
				resultado.append(palabra1[:i:].upper()+palabra2[:j:].upper()+palabra3[:k:].upper())
	return resultado
	
#Esta no funcion no se aplico en la implementacion, pero si puede usarse
def agregaNumeros(lista):
	'''
	Funcion que regresa una lista de nuevos passwords a partir de una lista
	de palabras mezclando estas con los numeros mas usados en passwords
	'''
	nueva=lista
	secNumeros= {'123','000','0000','123456','4321','246','666','1111','000000','0123','098','987'}
	for palabra in lista:
		for cad in secNumeros:
			print 'esta generando: '+palabra+cad
			nueva.append(palabra+cad)
			nueva.append(cad+palabra)
	return nueva



if __name__ == '__main__':

	archivo = sys.argv[1]
	claves=[]
	with open(archivo,'r') as leido: #Se lee el archivo con la lista de palabras
		palabras=leido.read()
		claves=palabras.splitlines()
	print 'Comenzaron a generarse'
	#Se obtiene la primera generacion de passwords
	listaComb=combinaciones(claves[0],claves[1],claves[2])
	final=listaComb
	#Se obtiene la segunda generaciond e passwords
	generacion=crea_generacion(listaComb)
	final+=generacion
	#Se obtiene el resto de generaciones y se genera el archivo donde se guardan
	with open('generadas.txt', 'a') as este:
		for pal in final:
			este.write(pal+'\n')
		while generacion !=[]:
			generacion=crea_generacion(generacion)
			final+=generacion
			print 'se generaron %d nuevos passwords' %(len(generacion))
		final=set(final)
		print 'Se crearon %d passwords' %(len(final))
		for pal in final:
			este.write(pal+'\n')
