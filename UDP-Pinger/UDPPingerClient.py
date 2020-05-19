
import time
from socket import *
import sys

# Server hostname and port as command line arguments
host = sys.argv[1]
port = sys.argv[2]
timeout = 1 # in seconds

# UDP client socket
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(timeout)

# Sequence number of the ping message
ptime = 0

# Ping 10 times
while ptime < 10:
    ptime += 1
    sentTime=time.time()
    data = "PING {} {}".format(ptime, sentTime)

    try:
        clientSocket.sendto(data.encode(),(host,int(port)))
        response,address=clientSocket.recvfrom(2048)
        recvTime= time.time()
        print("Response", response)
        print("Round trip time",recvTime-sentTime)

    except Exception as e:
    # Server does not respond
	# Assume the packet is lost
        print(e)
        continue

# Close the client socket
clientSocket.close()
