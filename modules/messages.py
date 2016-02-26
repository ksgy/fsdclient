import socket
import sys
import time

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Messages:
	
	def __init__(self):
		pass
		
	@staticmethod
	def start(message, sock):

		print >>sys.stderr, 'sending "%s"' % message
		sock.sendall(message)

		run = True

		while run:
			try:
				# @<transponder flag>:<callsign&gt:<squawk code>:1:<latitude>:<longitude>:<altitude>:<speed>:<heading>:0
				message = '@S:MIS:1200:1:19.424633:-99.077919:7335:100:4290775416:-329\r\n'
				# print >>sys.stderr, 'sending "%s"' % message
				sock.sendall(message)
				time.sleep( 5 )

			except socket.timeout:
				print("timeout error")
			except socket.error:
				print("socket error occured: ")
			except Exception as inst:
				print type(inst)	
				print inst.args	
				print inst	

		print 'end'