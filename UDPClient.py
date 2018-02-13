import socket  # for sockets
import sys  # for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

try:
    ip_address = sys.argv[1]
    port_number = int(sys.argv[2])
    expression = sys.argv[3]
except:
    raise Exception("Error occurred while reading parameters")

while 1:
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
                s.sendto(message, (ip_address, port_number))
                d = s.recvfrom(1024)
                data = d[0]
                addr = d[1]
            except socket.error, msg:
                print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()
            stack.append(float(data))
        else:
            stack.append(float(tk))
    break
print data
s.sendto("exit", (ip_address, port_number))