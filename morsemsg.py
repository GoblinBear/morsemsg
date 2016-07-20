#!/usr/bin/python
# 0 = dot
# 1 = dash

import socket
import thread
import time

#======== encrypt =====================================

def encrypt(letter):
	emap = {'a' : '01'   ,
			'b' : '1000' ,
			'c' : '1010' ,
			'd' : '100'  ,
			'e' : '0'    ,
			'f' : '0010' ,
			'g' : '110'  ,
			'h' : '0000' ,
			'i' : '00'   ,
			'j' : '0111' ,
			'k' : '101'  ,
			'l' : '0100' ,
			'm' : '11'   ,
			'n' : '10'   ,
			'o' : '111'  ,
			'p' : '0110' ,
			'q' : '1101' ,
			'r' : '010'  ,
			's' : '000'  ,
			't' : '1'    ,
			'u' : '001'  ,
			'v' : '0001' ,
			'w' : '011'  ,
			'x' : '1001' ,
			'y' : '1011' ,
			'z' : '1100' ,
			' ' : ' '
		}

	return emap[letter]

#======== decrypt =====================================

def decrypt(morse):
	dmap = {'01'    : 'a' ,
			'1000'  : 'b' ,
			'1010'  : 'c' ,
			'100'   : 'd' ,
			'0'     : 'e' ,
			'0010'  : 'f' ,
			'110'   : 'g' ,
			'0000'  : 'h' ,
			'00'    : 'i' ,
			'0111'  : 'j' ,
			'101'   : 'k' ,
			'0100'  : 'l' ,
			'11'    : 'm' ,
			'10'    : 'n' ,
			'111'   : 'o' ,
			'0110'  : 'p' ,
			'1101'  : 'q' ,
			'010'   : 'r' ,
			'000'   : 's' ,
			'1'     : 't' ,
			'001'   : 'u' ,
			'0001'  : 'v' ,
			'011'   : 'w' ,
			'1001'  : 'x' ,
			'1011'  : 'y' ,
			'1100'  : 'z' ,
			' '     : ' '
		}

	return dmap[morse]

#======== sender =====================================

def sender(recvaddr):
	
	while True:
		flag = 0
		inputStr = raw_input()
		
		#check invalid letter
		for i in range(0, len(inputStr)):
			if (not inputStr[i].islower()) and (not inputStr[i]==' ') :
				flag = 1
				print 'Error: Invalid letter, massage no send'
				break
		if flag == 1:
			continue

		cipher = encrypt(inputStr[0]) + '.'
		for i in range(1, len(inputStr)):
			if i<len(inputStr)-1:
				cipher = cipher + encrypt(inputStr[i]) + '.'
			else:
				cipher = cipher + encrypt(inputStr[i])
			
		recvsock.send(cipher)
		
	recvsock.close()
	
#======== receiver =====================================

def receiver(s):

	while True:
		
		cipher = s.recv(1024)
		

		item = cipher.strip().split('.')

		plaintext =  decrypt(item[0])
		for j in range(1, len(item)):
			plaintext = plaintext + decrypt(item[j])

		print 'A(ciphertext):',cipher
		print 'A(plaintext):',plaintext

	s.close()

#======== main =====================================

#inputStr = raw_input()

#create sender socket
s1 = socket.socket()
host1 = '192.168.1.124'
port1 = 12341
s1.bind((host1, port1))

s1.listen(5) 

recvsock, recvaddr = s1.accept() 
print 'Got connection from A',  recvaddr

#create receiver socket
s2 = socket.socket()
host2 = '192.168.1.2' # host2 = socket.gethostname()
port2 = 12342

s2.connect((host2, port2))
#This put in lab




#receive or send message
try:
   thread.start_new_thread( receiver, (s2,) )
   thread.start_new_thread( sender, (recvaddr,) )
except:
   print "Error: unable to start thread"

while 1:
   pass






