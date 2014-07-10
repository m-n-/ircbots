import irc
import irc.client
import threading
import time

client = irc.client.IRC()
server = client.server()
server.connect("irc.freenode.net", 6667, "cbot1")



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

def onrecieve(_, evt):
	print(evt.source + ": " + uncrypt(" ".join(evt.arguments)))

client.add_global_handler("privmsg", onrecieve)


def send_msg():
	# while 1:
	msg = input("")
	encrypted_msg = encrypt(msg)
	server.privmsg("cbot2", encrypted_msg)


	
#get_msg()
runner = threading.Thread(target=lambda: client.process_forever())
runner.start()

#send_msg()
# send_thread = threading.Thread(target=send_msg)
# send_thread.start()

while 1:
	send_msg()
	# time.sleep(1)