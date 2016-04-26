from SimpleXMLRPCServer import SimpleXMLRPCServer
from random import randint

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_introspection_functions()

class GuessGame:
    def newNumber(self):
        self.number = randint(0, 100)
    def guess(self, number):
        if number < self.number:
            return "bigger than this"
        elif number > self.number:
            return "smaller than this"
        else:
            return "true guess!!!"

server.register_instance(GuessGame())
server.serve_forever()