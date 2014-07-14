import irc
import irc.client
import threading
import time
from Crypto.Cipher import AES
import base64

client = irc.client.IRC()
server = client.server()
server.connect("irc.freenode.net", 6667, "cbot1")


#use AES encryption for 16 bit encryption
obj=AES.new('1qazxsw23edcvfr4')


#basic encryption add 4 and subtract 4 to message string
'''
def uncrypt(encrypted_string): #un-encrypt incoming messages
	unencrypted_string = ""
	for c in encrypted_string:
		unencrypted_string += chr(ord(c) + 4)
	return unencrypted_string

def encrypt(unencrypted_string):
	encrypted_string = ""
	for c in unencrypted_string:
		encrypted_string += chr(ord(c) - 4)
	return	encrypted_string
'''

def onrecieve(_, evt): #process recieved message with decrypt and utf-decode >> strip white space with strip()
	recieved_msg = base64.b64decode("".join(evt.arguments))
	print(evt.source + ": " + obj.decrypt(recieved_msg).decode("utf-8").strip())

#add handler to wait for recieved privmsg
client.add_global_handler("privmsg", onrecieve)


def send_msg(): #process sent message to make sure msg is 16 chars 
	msg = input("")

	if (len(msg) < 16):
		times = 16 - len(msg)
		for i in range(1, times+1):
			msg += " "

	elif ((len(msg) % 16) != 0):
		times = 16 - (len(msg) % 16)
		for i in range(1, times+1):
			msg += " "

	#encrypt message and encode to b64 and utf-8		
	encrypted_msg = base64.b64encode(obj.encrypt(msg)).decode("utf-8")
	server.privmsg("cbot2", encrypted_msg)


	
#create thread to make sure the two processes run independently of each other so send and recieve can work in tandem
runner = threading.Thread(target=lambda: client.process_forever())
runner.start()

#send_msg()
# send_thread = threading.Thread(target=send_msg)
# send_thread.start()

while 1:
	send_msg()