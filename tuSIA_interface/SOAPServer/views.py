from wsgiref.validate import validator
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Integer, Double, String, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

import json

from spyne import Iterable, Array
from spyne import ComplexModel
from django.forms.models import model_to_dict
# from apps.comun.always.SerchFilter import keys_add_none
from spyne.error import ResourceNotFoundError
from spyne.model.fault import Fault
from django.db.models.deletion import ProtectedError

from .data import getAllCourses



# class Cursos(ComplexModel):
#     Id_subject = Integer,
#     Name_subject = String,
#     Credits = Integer,
#     Description = String,


class SoapService(ServiceBase):

    @rpc(_returns=Array(AnyDict))
    def getcourses(ctx):
        allCourses = getAllCourses()
        return allCourses
        # llamar a la funcion de data que trae todos los cursos

    # @rpc(Double(), Double(), _returns=Double)
    # def getCourseById():
    #   pass


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)


def consulta():
    django_soap_app = DjangoApplication(soap_app)
    my_soap = csrf_exempt(django_soap_app)
    return my_soap
