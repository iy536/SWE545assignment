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

        # data = c.recv(1024)
        number = random.randint(1, 10)
        wellcome = ("Welcome to the guess the number game!\n")
        bt = ("Bigger than this\n")
        st = ("Smaller than this\n")
        guess = ("What is your guess? ")
        guessed = ("True Guess!!!\n")
        c.sendall(wellcome)
        while True:

            c.send(guess)
            guessTaken = int(c.recv(1024))
            if guessTaken < number:
                c.sendall(bt)
                guessTaken = int(c.recv(1024))
            elif guessTaken > number:
                c.sendall(st)
                guessTaken = int(c.recv(1024))
            else:
                # c.send(guessed)
                # c.send("Would you like to continue yes = 1, no =0 :")
                c.sendall("1")
                # yes = int(c.recv(1024))
                # if (yes == 1):
                #     number = random.randint(1,10)
                # else:
                #     c.close()