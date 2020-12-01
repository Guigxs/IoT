# from network import LoRa
# import ubinascii
# import socket
# import time
# import json

# lora = LoRa()
# print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))

# lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# # create an OTAA authentication parameters, change them to the provided credentials
# app_eui = ubinascii.unhexlify('70B3D57ED003839F')
# app_key = ubinascii.unhexlify('69CD1693FF4AF4B5B508B62DE90FD06C')

# # join a network using OTAA (Over the Air Activation)
# #uncomment below to use LoRaWAN application provided dev_eui
# lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
# #lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# # wait until the module has joined the network
# while not lora.has_joined():
#     time.sleep(2.5)
#     print('Not yet joined...')

# print('Joined')

# # create a LoRa socket
# s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# # set the LoRaWAN data rate
# s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# s.bind(1)

# # make the socket blocking
# # (waits for the data to be sent and for the 2 receive windows to expire)
# s.setblocking(True)

# # send some data

# s.send(bytes([0x56, 0x77, 0x89, 0xFF, 0xA6, 0xAA, 0x01, 0x02, 0x03, 0x01, 0x02, 0x03,]))


# # make the socket non-blocking
# # (because if there's no data received it will block forever...)
# s.setblocking(False)

# # get any data received (if any...)
# data = s.recv(64)
# print(data)



from machine import UART
import time
uart = UART(1, 9600,pins=('P20','P21'))                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters
time.sleep(1)
uart.write("hello")
time.sleep(1)
uart.read(5)
print(uart.any()  )             # returns the number of characters available for reading

print("coucou 2")

# import machine
# import time
# from machine import Pin
# from math import pi


# while True:

# #vers oscillo : 4095
# #verls landry : 3566
# #vers thomas : 957


#     time.sleep(2.5)

#     adc = machine.ADC()             # create an ADC object
#     apin = adc.channel(pin='P16')   # create an analog pin on P16
#     val = apin()                    # read an analog value
#     print(val)
#     if( 3600 <= val):
#         print("Nord")
    
#     elif( 800 < val < 1500):
#         print("Est")
    
#     elif(3000 < val < 3600):
#         print("Sud")
    
#     elif(2500 < val < 5000):
#         print("Est")

    
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
    
    print("Vitesse : ",(flancMontant/5)*2*pi)
    print("----------------")
