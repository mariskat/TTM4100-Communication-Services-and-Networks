
from socket import *
import argparse as ap
import getpass as gp

#Sender_email and recipient_email as arguments in command line
parser = ap.ArgumentParser(description='A test SMTP client without authentication')
parser.add_argument('-f', '--from', dest='fromMail', required=True, metavar='<sender_email>')
parser.add_argument('-t', '--to', dest='toMail', required=True, metavar='<recipient_email>')

args = parser.parse_args()
fromMail = args.fromMail #Sender email address
toMail = args.toMail #Recipient email address

# Message to send
msg = "\r\n Message sent"
endmsg = "\r\n.\r\n"

mailserver = 'localhost'

#Creating socket, establishing TCP connection
serverName = 'mailServer'
serverPort = 2525
clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM: TCP socket, AF_INET: IPv4
clientSocket.connect((mailserver,serverPort))

recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')

# Sending HELO command and printing server response
heloCommand = 'EHLO Hey\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')

# Sending MAIL FROM command and printing server response
mailFromCommand = 'MAIL FROM: <{}> \r\n'.format(fromMail)
clientSocket.send(mailFromCommand.encode()) #Python 3

recv2 = clientSocket.recv(1024)
print('Mail from: ', recv2)
if recv2[:3] != '250':
	print ('250 reply not received from server.')

# Sending RCPT TO command and printing server response
RCPTtoCommand = 'RCPT TO: <{}> \r\n'.format(toMail)
clientSocket.send(RCPTtoCommand.encode())

recv3 = clientSocket.recv(1024)
print('RCPT to: ', recv3)
if recv3[:3] != '250':
	print ('250 reply not received from server.')

# Sending DATA command and printing server response
DataCommand = 'DATA \r\n'
clientSocket.send(DataCommand.encode())

recv4 = clientSocket.recv(1024)
print('Data: ', recv4)

# Sending message data
clientSocket.send(msg.encode())

# Message ends with a single period
dot = '\r\n.\r\n'
clientSocket.send(dot.encode())

# Sending QUIT command and getting server response
quitCommand = 'QUIT \r\n'
clientSocket.send(quitCommand.encode())
recv4 = clientSocket.recv(1024)
