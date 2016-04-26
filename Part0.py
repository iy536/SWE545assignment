import xmlrpclib
import random

class Sample():
    def setServer(self, server):
        self.server = server


    def selectTwoNumbers(self):
        string1, self.number1 = self.server.test.guess()
        string2, self.number2 = self.server.test.guess()
        self.number3 = random.randint(1,100)
        print "First Number: ", string1,  self.number1
        print "Second Number: %d" % self.number2
        print "Third Number: %d" % self.number3

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
