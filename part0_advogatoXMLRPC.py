import xmlrpclib
import random

class Sample():
    def setServer(self, server):
        self.server = server


    def selectTwoNumbers(self):
        # Select first random number btwn 1 t0 100
        self.number1 = random.randint(1, 100)

        # Select second random number btwn 1 t0 100
        self.number2 = random.randint(1, 100)

        # Test Server's guess() fumction
        string3, self.number3 = self.server.test.guess()

        print "First Number: %d" % self.number1
        print "Second Number: %d" % self.number2
        print "Server guess() ==> ", string3, self.number3

    def sumTwoNumbers(self):
		sum , product = self.server.test.sumprod(self.number1, self.number2)
		print "Sum : %d " % sum

    def productTwoNumbers(self):
		sum , product = self.server.test.sumprod(self.number1, self.number2)
		print "Product : %d " % product

s = Sample()
server = xmlrpclib.Server("http://www.advogato.org/XMLRPC")
s.setServer(server)
s.selectTwoNumbers()
s.sumTwoNumbers()
s.productTwoNumbers()
