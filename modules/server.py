import socket, select, string, sys

class Server:
	
	def __init__(self):
		pass
		
	@staticmethod
	def start():
	
		host = 'localhost'
		port = 51000
		 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(10)
		 
		# connect to remote host
		try :
			s.connect((host, port))
		except :
			print 'Unable to connect'
			sys.exit()
		 
		print 'Connected to remote host'
		 
		while 1:
			socket_list = [sys.stdin, s]
			 
			# Get the list sockets which are readable
			read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
			 
			for sock in read_sockets:
				#incoming message from remote server
				if sock == s:
					data = sock.recv(4096)
					if not data :
						print 'Connection closed'
						sys.exit()
					else :
						#print data
						sys.stdout.write(data)
				 
				#user entered a message
				else :
					msg = sys.stdin.readline()
					s.send(msg)