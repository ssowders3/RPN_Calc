"""
RPN calculator implementation.
"""
import sys
import socket

BUFFER_SIZE = 4096
MESSAGE = "exit"

try:
    ip_address = sys.argv[1]
    port_number = int(sys.argv[2])
    expression = sys.argv[3]
except:
    raise Exception("Error occurred while reading parameters")
tokens, stack = expression.split(' '), []
for tk in tokens:
    if tk == '+' or tk == '-' or tk == '*' or tk == '/' or tk == "^":
        try:
            operand1 = str(stack[-2])
            operand2 = str(stack[-1])
        except:
            raise Exception("Unable to pop operands off Stack due to invalid Expression input")
        message = str(operand1 + " " + operand2 + " " + tk)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_address, port_number))
        except socket.error:
            raise Exception("Client was unable to connect to Server")
        try:
            s.send(message)
        except socket.error:
            raise Exception("Client was unable to send message to Server")
        try:
            data = s.recv(BUFFER_SIZE)
        except socket.error:
            raise Exception("Client was unable to receive messages from Server")
        stack.append(float(data))
        s.close()
    else:
        stack.append(float(tk))
try:
    print data
except:
    raise Exception("Invalid expression provided")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port_number))
except socket.error:
    raise Exception("Client was unable to connect to Server")
try:
    s.send(MESSAGE)
except socket.error:
    raise Exception("Client was unable to send message to Server")
s.close()