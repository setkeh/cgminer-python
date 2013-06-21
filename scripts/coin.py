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
s.send(json.dumps({"command":"coin","parameter":"Network Difficulty"}))    
response = linesplit(s)
response = response.replace('\x00','')
response = json.loads(response)
def hash_method():
    return response['COIN'][0]['Hash Method']
def current_block_hash(): 
    return response['COIN'][0]['Current Block Hash']
def long_poll():
	return response['COIN'][0]['LP']
def diff():
	return response['COIN'][0]['Network Difficulty']
s.close()
