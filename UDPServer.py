import socket
import math
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    raise Exception("Unable to create socket")
server_port = 12000
try:
    server = (socket.gethostname(), server_port)
except socket.gaierror:
    raise Exception("Unable to get host name")
try:
    sock.bind(server)
except socket.error:
    raise Exception("Unable to bind socket")
while True:
    d = sock.recvfrom(1024)
    data = d[0]
    addr = d[1]

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
        sock.sendto(str(stack[0]), addr)
    except socket.error:
        raise Exception("Unable to send to client")