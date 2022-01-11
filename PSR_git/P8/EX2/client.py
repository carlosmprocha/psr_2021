#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time
import dog_lib

# dog = dog_lib.Dog(name='Toby', age=7, color='brown')  # instantiate a new dog
# dog.addBrother('Lassie')
# dog.addBrother('Boby')
# print('CLIENT: my dog has ' + str(dog))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23458)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example data to be sent to the server

# create a dog instance
dog = dog_lib.Dog('boby', 'brown', 7)
dog.addBrother('Lassie')
dog.addBrother('Max')

print(dog)

messages = []
messages.append(dog.name)
messages.append(',')
messages.append(dog.color)
messages.append(',')
messages.append(str(dog.age))
for brother in dog.brothers:
    messages.append(',')
    messages.append(brother)

print(messages)
text_to_send = ''.join(messages)
print(text_to_send)

message_formated=str(text_to_send).encode("utf-8")
sock.sendall(message_formated)
time.sleep(2)  # wait for two seconds

# for message in messages:
#     print('Sending message: ' + str(message))
#     message_formated = str(message).encode("utf-8")
#     sock.sendall(message_formated)
#     time.sleep(2)  # wait for two seconds

sock.close()  # close connection
