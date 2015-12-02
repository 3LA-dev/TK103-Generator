# TK103-Generator
Tester framer TK103 in Python

This script is limited to 3 basic operations:
- BP05  Message logging
- BR00  Ping or Data GPS
- BO01  Alarm message

##Starter
Clone the repository
```
git clone https://github.com/3LA-dev/TK103-Generator.git
cd TK103-Generator
```

Run the script with python

```
python generator.py
```

## Settings
by default the script will connect to a TCP socket in local host on port 8090, to change the settings in the script edit the following line

```
# Data Server....
HOST = '127.0.0.1'
PORT = 8090
```

You can change the device settings by editing the script

```
#Data device
tracker_id  =   '527721199947'              #Message tracking, may be the date
device_id   =   '000017721199947'           # 0000 + telephone number
latitud     =   '2007.2384N'                #dddmm.mmmm format 
longitud    =   '09844.2176W'
date        =   time.strftime('%y%m%d')     #YYMMDD
availability =  'A'
speed       =   '128.5'                     #km/h
times       =   time.strftime('%H%M%S')     #HHMMSS
orientation =   '185.21'
IO_State    =   '1000000A' 
#1st power 1 = power off or on battery And 0 = power On or on external power supply
#2nd ACC (ignition) 0 = off and 1 = on
#others are reservations Like, 3rd AC
#4th not needed
#5th GPS
milepost    =   'L'
mile_data   =   '00000000'                  #Mileage data Max is OxFFFFFFFF
```
