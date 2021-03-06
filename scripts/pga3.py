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
s.send(json.dumps({"command":"pga","parameter":"3"}))    
response = linesplit(s)
response = response.replace('\x00','')
response = json.loads(response)
def p3_mhs():
    return response['PGA'][0]['MHS av']
def p3_accepted(): 
    return response['PGA'][0]['Accepted'] 
def p3_rejected(): 
    return response['PGA'][0]['Rejected']
def p3_hwerrors():
    return response['PGA'][0]['Hardware Errors']
def p3_utility():
    return response['PGA'][0]['Utility']
s.close()
