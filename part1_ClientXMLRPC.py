import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8000/")

try:
    server.newNumber()
except xmlrpclib.Fault as err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString

while 1:
    number = input("Enter number: ")
    result = server.guess(number)
    print result
    if "true guess!!!" == result:
        break
