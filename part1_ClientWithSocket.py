import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.connect(("localhost", 12345))
    recvdata = s.recv(1024)
    print(recvdata)
    while(1): #Setting a loop
        userInput = raw_input(">")
        s.send(userInput + '\r\n\r\n')
        recvdata = s.recv(1024)
        print(recvdata)
        if "Your guess is correct" == recvdata :
            print("Connection closing...")
            # s.shutdown(0)
            s.close()

except KeyboardInterrupt:
    print("\nConnection close")
    sys.exit()