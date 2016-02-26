import socket
import sys
import time
import os

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
				with open(os.path.join('i:/','XPlane10','Resources','plugins','FlyWithLua','Scripts', 'fsdclient.txt'), 'r') as f:
					flightinfo = f.readline()

				# xpdr_f .. "|" .. xpdr .. "|" .. alt .. "|" .. lat .. "|" .. lon .. "|" .. spd .. "|" .. hdg)

				s = flightinfo.split('|')
				print flightinfo
				xpdr_f = 'S'
				if (s[0] == '2'):
					xpdr_f = 'N'					

				xpdr = s[1] 
				alt = s[2]
				lat = s[3]
				lon = s[4]
				spd = s[5]
				hdg = s[6]
				callsign = s[7]
				password = s[8]
				homebase = s[9]
				# @<transponder flag>:<callsign&gt:<squawk code>:1:<latitude>:<longitude>:<altitude>:<speed>:<heading>:0

				message = '@'+xpdr_f+':'+callsign+':'+xpdr+':1:'+('{0:.6f}'.format(float(lat)))+':'+('{0:.6f}'.format(float(lon)))+':'+str(int(float(alt)))+':'+str(int(float(spd)))+':4290775416:-329\r\n'
				print >>sys.stderr, 'sending "%s"' % message
				sock.sendall(message)
				time.sleep(1)

			except socket.timeout:
				print("timeout error")
			except socket.error:
				print("socket error occured: ")
			except Exception as inst:
				print type(inst)	
				print inst.args	
				print inst	

		print 'end'