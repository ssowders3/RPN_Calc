"""
RPN calculator implementation.
"""
import sys
import socket

BUFFER_SIZE = 1024
MESSAGE = "exit"

ip_address = sys.argv[1]
port_number = int(sys.argv[2])
expression = sys.argv[3]

tokens, stack = expression.split(' '), []

for tk in tokens:
    if tk == '+' or tk == '-' or tk == '*' or tk == '/' or tk == "^":
        operand1 = str(stack[-2])
        operand2 = str(stack[-1])
        message = str(operand1 + " " + operand2 + " " + tk)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port_number))
        s.send(message)
        data = s.recv(BUFFER_SIZE)
        stack.append(float(data))
        s.close()
    else:
        stack.append(float(tk))

print "received data: ", data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port_number))
s.send(MESSAGE)
s.close()