#!/usr/bin/env python
import socket
import os
import time

# Data Server....
HOST = '127.0.0.1'
PORT = 8090
ADDR = (HOST, PORT)

#Data device
tracker_id 	= 	'527721199947' 				#Message tracking, may be the date
device_id 	= 	'000017721199947' 			# 0000 + telephone number
latitud 	= 	'2007.2384N' 				#dddmm.mmmm format 
longitud 	=	'09844.2176W'
date 		= 	time.strftime('%y%m%d') 	#YYMMDD
availability = 	'A'
speed 		= 	'128.5' 					#km/h
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

# TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'connecting to %s port %s' % ADDR
sock.connect(ADDR)

try:
	while True:
		os.system('clear')
		print('            Host: %s port: %s'%ADDR)
		print('''==================================================
::::::::::::::::Generator::TK103::::::::::::::::::
==================================================
                    Commands
__________________________________________________

/login --- BP05  Message logging
/ping  --- BR00  Ping or Data GPS
/alarm --- BO01  Alarm message
			''')
		comando = raw_input('>>')
		os.system('clear')
		print('            Host: %s port: %s'%ADDR)
		print('''
==================================================
::::::::::::::::Generator::TK103::::::::::::::::::
==================================================''')
#::::::::::::::::::::::::::::::::::::::::::::::: Message logging
		if (comando == '/login'):
			print('''::::::::::::::::::::/login::::::::::::::::::::::::''')
			message = '('+tracker_id+'BP05'+device_id+GPS_Data+')'
			print '\n________________Frame: \n\n%s' % message
			sock.sendall(message)
			data = sock.recv(1024)
			if data:
				print '\n________________Answer:\n\n%s' % data
#::::::::::::::::::::::::::::::::::::::::::::::: Ping or Data GPS
		elif (comando == '/ping'):
			print('''::::::::::::::::::::/ping::::::::::::::::::::::::''')
			message = '('+tracker_id+'BR00'+GPS_Data+')'
			print '\n________________Frame: \n\n%s' % message
			sock.sendall(message)
#::::::::::::::::::::::::::::::::::::::::::::::: Alarm message
		elif (comando == '/alarm'):
			print('''::::::::::::::::::::/alarm::::::::::::::::::::::::''')
			print('''                Codigos de Alarma
0 - vehicle Off
1 - Accident
2 - SOS
3 - Stolen alarm
4 - Low Speed
5 - High speed
6 - Alarm Geo-Fence''')
			x=raw_input('>> ')
			message = '('+tracker_id+'BO01'+x+GPS_Data+')'
			print '\n________________Frame: \n\n%s' % message
			sock.sendall(message)
			data = sock.recv(1024)
			if data:
				print '\n________________Answer:\n\n%s' % data
#:::::::::::::::::::::::::::::::::::::::::::::::::::: wrong command...
		else:
			print'-------- Alert!: Invalid command'
			time.sleep(2)
		raw_input('\n*Press Enter to continue...')

finally:
	sock.close()
