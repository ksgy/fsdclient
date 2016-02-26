# ez a jo :)
from modules import server
from modules import messages

import socket
import time
import threading
import sys, os, traceback, types
import select
from random import randint

TCP_IP = '88.151.99.237'
TCP_PORT = 6809
BUFFER_SIZE = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

s = server.Server()
m = messages.Messages()

def _testserver():
	s.start()

def _testmessage():
	m.start('#APMIS:SERVER::MIS:1:9:11:MISU..#WXMIS:SERVER:LHBP..$AXMIS:SERVER:METAR:LHBP\r\n', sock)
	
ServerThread = threading.Thread(target=_testserver, args=())
MessagesThread = threading.Thread(target=_testmessage, args=())
e = threading.Event()

ServerThread.start()
MessagesThread.start()

