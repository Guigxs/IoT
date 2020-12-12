from network import LoRa
import ubinascii
import socket
import time
import cayenneLPP
import machine
from machine import Pin
from math import pi
import pycom

pycom.heartbeat(False)

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify('70B3D57ED003839F')
app_key = ubinascii.unhexlify('69CD1693FF4AF4B5B508B62DE90FD06C')

start = time.time()
now = start

while(True):
    if (now - start) > 60:
        start = now
        lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

        adc = machine.ADC()             # create an ADC object
        apin = adc.channel(pin='P16')   # create an analog pin on P16
        val = apin()                    # read an analog value

        if( 3600 <= val):
            # print("Nord")
            direction = 1

        elif( 800 < val < 1500):
            # print("Est")
            direction = 2

        elif(3000 < val < 3600):
            # print("Sud")
            direction = 3

        else:
            # print("Error")
            direction = -1
        # elif(2500 < val < 5000):
        #     print("Est")
        #     direction = 2


        beginTime = time.time()
        actualTime = time.time()
        flancMontant = 0
        flanMontantexcecute = False
        pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_DOWN)

        while( beginTime + 5 > actualTime):
            pine = pin()   # fast method to get the value
            if (pine ==0):
                flanMontantexcecute = False
            
            if(flanMontantexcecute == False):
                if( pine ==1):
                    flancMontant +=1
                    flanMontantexcecute = True
            actualTime = time.time()

        vitesse = (flancMontant/5) * 2 * pi * 0.07


        while not lora.has_joined():
            time.sleep(2.5)
            print('Not yet joined...')

        print('Joined')

        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

        s.setblocking(True)

        lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)
        lpp.add_analog_input(direction, 4)
        lpp.add_analog_input(vitesse)
        lpp.add_gps(40.434343, 8.545454, 0)
        lpp.set_socket(s)
        lpp.send()

        s.setblocking(False)

    now = time.time()
