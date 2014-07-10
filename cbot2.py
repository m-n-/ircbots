import irc
import irc.client

client = irc.client.IRC()
server = client.server()
server.connect("irc.freenode.net", 6667, "cbot2")

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

client.add_global_handler("privmsg", onrecieve)
client.process_once(0.1)

while 1:
	msg = input(">")
	encrypted_msg = encrypt(msg)
	server.privmsg("cbot1", encrypted_msg)
	client.process_once(.2)

