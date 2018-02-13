import socket  # for sockets
import sys  # for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

try:
    ip_address = sys.argv[1]
    port_number = int(sys.argv[2])
    expression = sys.argv[3]
except:
    raise Exception("Error occurred while reading parameters")

try_count = 0
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
            while 1:
                try:
                    print try_count
                    if (try_count < 3):
                        s.sendto(message, (ip_address, port_number))
                        try_count = try_count + 1
                        s.settimeout(2)
                        d = s.recvfrom(4094)
                        data = d[0]
                        addr = d[1]
                        break

                except socket.timeout:
                    print 'send failed, trying again'
                    if try_count == 3:
                        print 'failed to send closing socket'
                        sys.exit()
            stack.append(float(data))
        else:
            stack.append(float(tk))
    break
print data
s.sendto("exit", (ip_address, port_number))