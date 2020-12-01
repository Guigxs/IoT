from network import LoRa
import ubinascii
import socket
import time

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('70B3D57ED003839F')
app_key = ubinascii.unhexlify('69CD1693FF4AF4B5B508B62DE90FD06C')

# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0xFF, 0x02, 0x03, 0x01, 0x02, 0x03, 0x01, 0x02, 0x03, 0x01, 0x02, 0x03,]))
start = [0xA2, 0x68, 0x76, 0x65, 0x6C, 0x6F, 0x63, 0x69, 0x74, 0x79] # {"velocity":
value1 = [10]
location = [0x68, 0x6C, 0x6F, 0x63, 0x61, 0x74, 0x69, 0x6F, 0x6E, 0xA2] #"location":{}
lat = [0x63, 0x6C, 0x61, 0x74, 0xFB]  # "lat":
a =  55.445544
# value2 = a.hex()
# long = [0x64, 0x6C, 0x6F, 0x6E, 0x67, 0xFB]  # "long":
# value3 = bytes(44.003344)
# direction = [0x69, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x69, 0x6F, 0x6E, 0x62] # "dircetion":
# value4 = list("SW".encode())

# s.send(bytes(value2)) # Start + bytes(string) + value

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)
