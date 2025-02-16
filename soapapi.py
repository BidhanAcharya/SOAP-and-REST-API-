from fastapi import FastAPI
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from starlette.middleware.wsgi import WSGIMiddleware

app = FastAPI()

# Define SOAP Service
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

# Create SOAP Application
soap_app = Application([CalculatorService], 'CalculatorService',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

# Wrap with WSGI
wsgi_app = WsgiApplication(soap_app)
app.mount("/soap", WSGIMiddleware(wsgi_app))

