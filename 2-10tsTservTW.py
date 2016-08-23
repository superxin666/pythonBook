from twisted.internet import  protocol, reactor
from  time import  ctime

PORT = 21567

class TSServProtocol (protocol.ProcessProtocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from', clnt)
    def dataReceiveed(self,data):
        self.transport.write('[%s] %s' %(ctime(),data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
