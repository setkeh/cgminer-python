#!/usr/bin/env python2.7

import socket
import json

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
s.connect(('192.168.1.6',4028))
s.send(json.dumps({"command":"pga","parameter":"9"}))    
response = linesplit(s)
response = response.replace('\x00','')
response = json.loads(response)
def p9_mhs():
    return response['PGA'][0]['MHS av']
def p9_accepted(): 
    return response['PGA'][0]['Accepted'] 
def p9_rejected(): 
    return response['PGA'][0]['Rejected']
def p9_hwerrors():
    return response['PGA'][0]['Hardware Errors']
def p9_utility():
    return response['PGA'][0]['Utility']
s.close()
