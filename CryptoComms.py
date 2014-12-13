#CryptoComms v1.0
#By DaKnOb

import os
import time

if(os.name=="nt"):          # Yes, it even runs on Windows
   os.system("cls")
else:
   os.system("clear")

print "**********************************************"
print "**************** CryptoComms *****************"
print "******************* v0.7 *********************"
print "**********************************************"
print "**** Encrypted P2P communcation by DaKnOb ****"
print "**********************************************"

from Crypto.PublicKey.RSA import RSAImplementation as RSA
import random

expo    =   [3,5,7,9,13,15,17,257,65537]    # A List of Public Exponents to use for your key
KEYSIZE =   2048                            # Your key size   

f = RSA()
myKey = f.generate(KEYSIZE, e=expo[random.randint(0,len(expo)-1)])



from SimpleXMLRPCServer import SimpleXMLRPCServer           # We are using an HTTP server to accept messages
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler   # We are using an HTTP browser to send messages

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
   rpc_paths = ('/RPC2',)

# Create server

ip = raw_input("IP Address: ")                              # Get the remote party IP Address
hostport = int(input("Host Port: "))                        # Get the local port to listen to
bcastport = int(input("Broadcast Port: "))                  # Get the remote port to send to

server = SimpleXMLRPCServer(("0.0.0.0", hostport),
                           requestHandler=RequestHandler,
                           logRequests=False)
server.register_introspection_functions()

# Register a function under a different name
def send(msg):

   global fKey
   n = msg.split()
   if(n[0]=="authnow"):
       print "Received Authentication Request. Sent Key."
       s.send("HS1 " + str(myKey.e) + " " + str(myKey.n))
   elif(n[0]=="HS1"):
       try:
           e = long(n[1])
           d = long(n[2])
           fKey = f.construct(tup=(d,e))
           if(fKey.can_encrypt()):
               print "Authenticated Successfully!"
           else:
               print "Received handshake but it is not valid."
       except:
           print "Received corrupted handshake."
   elif(n[0]=="ECD"):
       try:
           k = eval(msg[3:len(msg)])                    # Totally insecure, find a good way to replace it guys :P
           c = myKey.decrypt(k)
           print ("[" + str(time.strftime("%H:%M:%S")) + "]:" + str(c))
       except:
           print "Received corrupted message."
   else:
       print "*** Received improperly formatted message ***"
       print (str(msg))

   return "Gotcha"

def sendMsg(msg):
   m = msg.split()
   if(m[0]=="authnow"):
       try:
           s.send("authnow 1")
           print "Authentication Packet sent."
       except:
           print "Remote host did not reply."
   else:
       try:
           b = fKey.encrypt(msg, 64)
           b = str(b)
           s.send("ECD " + str(b))
       except:    
           print "Failed to send message. Type authnow to authenticate."
server.register_function(send, 'send')

import xmlrpclib
import threading



s = xmlrpclib.ServerProxy('http://' + str(ip) + ':' + str(bcastport))



def w(i):
   # Print list of available methods
   while(1):
       i = raw_input()
       if(i and i!="" and i!=" "):
           sendMsg(i)
       else:
           print "Cannot send this message."


def r(i):
   # Run the server's main loop
   server.serve_forever()





n = threading.Thread(target=w, args=[1])
n.start()
n = threading.Thread(target=r, args=[2])
n.start()
