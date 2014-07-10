import irc
import irc.client
from Crypto.Cipher import DES

client = irc.client.IRC()
server = client.server()
server.connect("irc.freenode.net", 6667, "cbot1")

obj=DES.new('yskcpd3d', DES.MODE_ECB)

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

def onrecieve(conneciton, evt):
	print(evt.source + ": " + uncrypt(" ".join(evt.arguments)))
'''

def onrecieve(conneciton, evt):
	print(evt.source + ": " + " ".join(evt.arguments))

client.add_global_handler("privmsg", onrecieve)
client.process_once(0.1)

while 1:
	msg = input(">")

	encrypted_msg = obj.encrypt(msg)
	server.privmsg("mnavarro", encrypted_msg)


	'''
	encrypted_msg = encrypt(msg)
	server.privmsg("cbot2", encrypted_msg)
	'''

	client.process_once(.2)

