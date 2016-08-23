from  twisted.internet import protocol, reactor
HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.ProcessProtocol):
    def sendData(self):
        data= input('< ')
        if data:
            print('...send %s' %data )
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()
    def dataReceived(self,data):
        print(data)
        self.sendData(data)

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clintConnectionFailed = \
        lambda  self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()