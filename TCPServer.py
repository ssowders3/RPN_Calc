import socket
import math
import sys

TCP_IP = '143.215.100.43'
TCP_PORT = 9090
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((TCP_IP, TCP_PORT))
# become a server socket
serversocket.listen(5)


while 1:
    conn, addr = serversocket.accept()
    data = conn.recv(BUFFER_SIZE)
    if data == "exit": break
    if not data: break
    tokens, stack = data.split(' '), []
    for tk in tokens:
        if tk == '+':
            stack = stack[:-2] + [stack[-2] + stack[-1]]
        elif tk == '-':
            stack = stack[:-2] + [stack[-2] - stack[-1]]
        elif tk == '*':
            stack = stack[:-2] + [stack[-2] * stack[-1]]
        elif tk == '/':
            stack = stack[:-2] + [stack[-2] / stack[-1]]
        elif tk == '^':
            stack = [stack[:-2] + stack[-2] ** stack[-1]]
        elif tk == 'ln':
            stack = stack[:-1] + [math.log([stack[-1]])]
        elif tk == 'log10':
            stack = stack[:-1] + [math.log10(stack[-1])]
        else:
            stack.append(float(tk))
    print "received data: ", data
    conn.send(str(stack[0]))
conn.close()

