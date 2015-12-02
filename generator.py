#!/usr/bin/env python
import socket
import os
import time

# Datos del servidor....
HOST = '127.0.0.1'
PORT = 8090
ADDR = (HOST, PORT)

#Datos generales Des dispositivo
tracker_id 	= 	'527721199947' 				#Seguimiento de mensaje, puede ser la fecha
device_id 	= 	'000017721199947' 			# 0000 + Numero Telefonico
latitud 	= 	'2007.2384N' 				#dddmm.mmmm formato 
longitud 	=	'09844.2176W'
date 		= 	time.strftime('%y%m%d') 	#YYMMDD
availability = 	'A'
speed 		= 	'128.5' 					#k/m por hora
times		= 	time.strftime('%H%M%S') 	#HHMMSS
orientation = 	'185.21'
IO_State 	= 	'1000000A' 
#1st power 1 = power off or on battery And 0 = power On or on external power supply
#2nd ACC (ignition) 0 = off and 1 = on
#others are reservations Like, 3rd AC
#4th not needed
#5th GPS
milepost 	=	'L'
mile_data 	= 	'00000000' 					#Mileage data Max is OxFFFFFFFF
GPS_Data = date+availability+latitud+longitud+speed+times+orientation+IO_State+milepost+mile_data

# Creando TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar a socket
print 'Conectando a %s puerto %s' % ADDR
sock.connect(ADDR)

try:
	while True:
		os.system('clear')
		print('            IP: %s Puerto: %s'%ADDR)
		print('''==================================================
::::::::::::::::Generador::TK103::::::::::::::::::
==================================================
                    Comandos
__________________________________________________

/login --- BP05  Mensaje de logeo
/ping  --- BR00  Ping o datos GPS
/alarm --- BO01  Mensaje de Alarma
			''')
		comando = raw_input('>>')
		os.system('clear')
		print('            IP: %s Puerto: %s'%ADDR)
		print('''
==================================================
::::::::::::::::Generador::TK103::::::::::::::::::
==================================================''')
#::::::::::::::::::::::::::::::::::::::::::::::: Mensaje de logeo
		if (comando == '/login'):
			print('''::::::::::::::::::::/login::::::::::::::::::::::::''')
			message = '('+tracker_id+'BP05'+device_id+GPS_Data+')'
			print '\n________________Trama: \n\n%s' % message
			sock.sendall(message)
			data = sock.recv(1024)
			if data:
				print '\n________________Respuesta:\n\n%s' % data
#::::::::::::::::::::::::::::::::::::::::::::::: Ping, Datos GPS
		elif (comando == '/ping'):
			print('''::::::::::::::::::::/ping::::::::::::::::::::::::''')
			message = '('+tracker_id+'BR00'+GPS_Data+')'
			print '\n________________Trama: \n\n%s' % message
			sock.sendall(message)
#::::::::::::::::::::::::::::::::::::::::::::::: Mensaje de Alarma
		elif (comando == '/alarm'):
			print('''::::::::::::::::::::/alarm::::::::::::::::::::::::''')
			print('''                Codigos de Alarma
0 - Vehiculo Apagado
1 - Accidente
2 - Vehiculo Robado (SOS)
3 - Alarma de Robado
4 - Velocidad Baja
5 - Velocidad Alta
6 - Alarama de Geo-Fence''')
			x=raw_input('>> ')
			message = '('+tracker_id+'BO01'+x+GPS_Data+')'
			print '\n________________Trama: \n\n%s' % message
			sock.sendall(message)
			data = sock.recv(1024)
			if data:
				print '\n________________Respuesta:\n\n%s' % data
#:::::::::::::::::::::::::::::::::::::::::::::::::::: Comando erroneo...
		else:
			print'-------- Alert!: Comando no valido'
			time.sleep(2)
		raw_input('\n*Presione Enter para continuar...')

finally:
	sock.close()
