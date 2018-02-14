import socket
import math
import sys

TCP_PORT = 12000
BUFFER_SIZE = 4096  # Normally 1024, but we want fast response
try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    raise Exception("Failed to create socket")
try:
    hostname = socket.gethostname()
except socket.gaierror:
    raise Exception("Failed to get host name")
try:
    serversocket.bind((hostname, TCP_PORT))
except socket.error:
    raise Exception("Failed to bind socket")
serversocket.listen(5)
while 1:
    conn, addr = serversocket.accept()
    try:
        data = conn.recv(BUFFER_SIZE)
    except:
        raise Exception("Unable to receive data from Client")
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
    try:
        conn.send(str(stack[0]))
    except socket.error:
        raise Exception("Unable to send connection to Client")
conn.close()

