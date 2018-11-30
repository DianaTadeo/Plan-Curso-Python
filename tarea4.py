#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#XML - parser
import sys
import hashlib
import csv
import xml.etree.ElementTree as ET
from datetime import datetime

md5_archivo=''
sha1_archivo=''
m5=hashlib.md5()
s1=hashlib.sha1()
hosts=[]
cadena=''

class Host():
	'''
	Clase que representa un host devuelto por nmap
	'''
	def __init__(self,address,prendido,sshp,eshoney,dominio):
		self.address=address
		self.prendido=prendido
		self.sshp=sshp
		self.eshoney=eshoney
		self.dominio=dominio


def lee_xml(archivo_nmap):
	'''
	Esta funcion se encarga unicamente de leer el archivo xml
	para despues regresar el arbol generado por la bilbioteca de xml.etree
	'''
	with open(archivo_nmap,'r') as nmap1:
		contenido = nmap1.read()
		m5.update(contenido)
		s1.update(contenido)
		return ET.fromstring(contenido)
		
def procesa(root):
	'''
	Esta funcion se encargara de realizar toda la recopialcion de informacion
	en cada puerto, tanto para imprimirla en pantalla, crear el archivo y
	generar las instancias de Host que se guardaran en una lista de Host's
	'''
	prendidos=0
	apagados=0
	ssh=0
	dns=0
	http=0
	https=0
	dominio=0
	apache=0
	honeypots=0
	ngix=0
	otro=0
	for host in root.findall('host'):
		#Variables necesarias para la creacion de instancias de Host
		estado_ssh=False
		es_honey=False
		prendido=False
		address=''
		nombre_dom=''
		#verificamos si el Host esta prendido
		if host.find('status').get('state') == 'up':
			prendidos+=1
			prendido=True
		else:
			apagados+=1
		#Recorremos las ramas del elemento 'host' del arbol
		for elem in list(host):
			if elem.tag == 'address': #Elemento '<address>'
				address= elem.get('addr')
			if elem.tag == 'hostnames': # Elemento '<hostnames>'
				for nombre in elem.iter():
					nombre_dom=nombre.get('name')
					if nombre_dom != None:
						dominio+=1 
			if elem.tag == 'ports': #Elemento '<ports>'
				for puerto in elem.iter('port'): # Elemento '<port ..'
					idport= puerto.get('portid') 
					estado= puerto.find('state').get('state') #Elemento '<state...'
					#Verificamos si los puertos 22,53,80 y 443 estan prendidos
					if idport== '22':
						if estado == 'open':
							ssh+=1
							estado_ssh=True
					if idport == '53':
						if estado== 'open':
							dns+=1
					if idport  == '80':
						if estado == 'open':
							http+=1
							# Verificamos que servidores http estan siendo usados
							if puerto.find('service').get('product') == 'Apache httpd':
								apache+=1
							elif puerto.find('service').get('product') == 'Dionaea Honeypot httpd':
								honeypots+=1
								es_honey=True
							elif puerto.find('service').get('product') == 'nginx':
								ngix+=1
							else:
								otro+=1
					if idport == '443':
						if estado== 'open':
							https+=1
		#Guardo el Host en la lista de Host's					
		hosts.append(Host(address,prendido,estado_ssh,es_honey,nombre_dom))
	cadena='Hora: '+str(datetime.now())
	cadena+= '\nMD5: '+m5.hexdigest()+'\nSHA1: '+s1.hexdigest()
	cadena+='\nHosts prendidos:'+ str(prendidos)+'\nHosts apagados:'+ str(apagados)+'\ncon puerto SSH abierto: '
	cadena+= str(ssh)+'\nCon puerto DNS abierto: '+ str(dns)+'\nCon puerto HTTP abierto: '+ str(http)+'\nCon puerto HTTPS abierto: '+ str(https)+'\nCon nombre de DOMINIO: '+ str(dominio)
	cadena+='\n______________________________________________'
	cadena+='\nApache: '+ str(apache)+'\nHoneypot (Dionea): '+ str(honeypots)+'\nNgix: '+ str(ngix)+'\nOtros: '+ str(otro)
	return cadena
	


def escribe_reporte(archivo_reporte, cadena):
	print cadena
	with open(archivo_reporte,'w') as output:
		output.write(cadena)

def genera_csv():
	with open('datos_nmap.csv','wb') as archivo:		
		output= csv.writer(archivo,dialect='excel')
		output.writerow(('IP Address','Nombre de Dominio','Encendido','SSH Abierto','Es Honeypot'))
		for host in hosts:
			val_encendido='No'
			val_ssh='No'
			val_honey='No'
			if host.prendido == True:
				val_encendido= 'Si'
			if host.sshp == True:
				val_ssh= 'Si'
			if host.eshoney==True:
				val_honey='Si'
			tupla= (host.address,host.dominio,val_encendido,val_ssh,val_honey)
			output.writerow(tupla)
	


if __name__ == '__main__':

    cad= procesa(lee_xml(sys.argv[1]))
    escribe_reporte('datos_nmap.txt',cad)
    genera_csv()
