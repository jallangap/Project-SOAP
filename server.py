from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class GreetingService(ServiceBase):
    @rpc(str, _returns=str)
    def say_hello(self, name):
        return f"Hello, {name}!"

application = Application([GreetingService], 
                          tns='soap.example.com',
                          in_protocol=Soap11(),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8000, wsgi_application)
    print("SOAP server is running...")
    server.serve_forever()
