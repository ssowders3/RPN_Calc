import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_port = 12000

server = ('143.215.100.43', server_port)
sock.bind(server)
print("Listening on " + socket.gethostname() + ":" + str(server_port))

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
    sock.sendto(str(stack[0]), addr)