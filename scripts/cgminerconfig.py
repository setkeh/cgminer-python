#!/usr/bin/env python2.7

import socket
import json
from settings import *

def linesplit(socket):
	buffer = socket.recv(4096)
	done = False
	while not done:
		more = socket.recv(4096)
		if not more:
			done = True
		else:
			buffer = buffer+more
	if buffer:
				return buffer

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((minerip(),minerport()))
s.send(json.dumps({"command":"config","parameter":"PGA"}))    
response = linesplit(s)
response = response.replace('\x00','')
response = json.loads(response)
def pga_count():
    return response['CONFIG'][0]['PGA Count']
def asic_count(): 
    return response['CONFIG'][0]['ASC Count'] 
def pool_count(): 
    return response['CONFIG'][0]['Pool Count']
def pool_stratergy():
    return response['CONFIG'][0]['Strategy']
def miner_os():
    return response['CONFIG'][0]['OS']
s.close()
