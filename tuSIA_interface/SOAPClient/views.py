from json import JSONDecodeError
from django.http import HttpResponse

import zeep


def index(request):
    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    print(client.service.Method1('Zeep', 'is cool'))

    return HttpResponse("Hello Geeks")

# traer la informacion con uncliente SoapService
# convertirla a JSON
# enviarla a GATEWAY
