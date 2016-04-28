import socket
import random


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 12345
s.bind((host,port))
s.listen(0)
print("Listening.....")

while True :
        c, addr = s.accept()
        print("Got Connection From ",addr)

        number = random.randint(1, 100)
        welcome = "Welcome to the guess the number game!\n"
        c.sendall(welcome)

        while True:
            guessTaken = (c.recv(1024))  + "\r\n"
            if not guessTaken: break
            else:

                if int(guessTaken) < number:
                    c.sendall("Bigger Than this")

                elif int(guessTaken) > number:
                    c.sendall("Smaller than this")

                else:
                    c.sendall("Your guess is correct")
                    c.close()


