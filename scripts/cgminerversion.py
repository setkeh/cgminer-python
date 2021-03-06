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
s.send(json.dumps({"command":"version","parameter":"CGMiner"}))    
response = linesplit(s)
response = response.replace('\x00','')
response = json.loads(response)
def cg_version():
    return response['VERSION'][0]['CGMiner']
def api_version(): 
    return response['VERSION'][0]['API'] 
s.close()
