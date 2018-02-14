RPN TCP and UDP Client Server Protocol
RPN citation: https://gist.github.com/avli/500d0ba1db8ba4c8a855

TCP Protocol

Run TCP from the client side: python TCPServer.py "local IP Address" 12000 "Expression string"

The local IP Address is the address of the machine you are running on, the port number is 12000 it is hardcoded on the
server side. The expression string is whatever expression that you want to be evaluated on the RPN calculator for example
"25 5 +" would be a simple example of something that this code should be able to handle. The Client starts by creating
the socket and attempts to connect to the server from the port and local ipaddress given from the command line arguements.
The server then accepts that connection and starts to listen for incoming client messages, the client sends a string to the
server of the first operation that the server needs to calculate. The server then replies with the calculation and the client
and server continue to communicate based on how many calculations need to be done. When all the calculations are done, the
client sends a "exit" string to the server to break out of the infinite while and end the program.


UDP Protocol
Run UDP from the client side: python UDPServer.py "local IP Address" 12000 "Expression string"

The local IP Address is the address of the machine you are running on, the port number is 12000 it is hardcoded on the
server side. The expression string is whatever expression that you want to be evaluated on the RPN calculator for example
"25 5 +" would be a simple example of something that this code should be able to handle. The Client starts by creating a socket
and the Server also creates a socket with the same host name and port number. The Client then attempts to send the first
operation to the server and if it cannot send to the server it sets a timeout of 2 seconds. If the Client times out it then
attempts again 3 times before exiting. Once it recieves the calculated operation back from the Server the Client and the
Server continue to communicate until the operation is complete. When the operation is completed the Client then sends a
"exit" string to the server to signal the server to exit the program.

