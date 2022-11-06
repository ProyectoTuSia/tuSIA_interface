from json import JSONDecodeError
from django.http import HttpResponse
from .data import getExternalCourses
from rest_framework.decorators import api_view
from rest_framework.response import Response

# def index(request):
#     wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
#     client = zeep.Client(wsdl=wsdl)
#     print(client.service.Method1('Zeep', 'is cool'))

#     return HttpResponse("Hello Geeks")

@api_view(['GET'])
def consulta(request):
    courses = getExternalCourses()
    return Response({"message": "Got some data!", "data": courses})
    
    # in this view the xml to json conversion should take place
    # a JSON should be returned to the GATEWAY

    # traer la informacion con uncliente SoapService
    # convertirla a JSON
    # enviarla a GATEWAY
