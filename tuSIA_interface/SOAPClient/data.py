import zeep
from zeep.transports import Transport
import json

wsdl = 'https://34.174.136.227:80/wsdl?wsdl'
transport = Transport()
transport.session.verify = False
settings = zeep.Settings(strict=False, xml_huge_tree=True,force_https=False)
client = zeep.Client(wsdl=wsdl, settings=settings, transport=transport)


def getExternalCourses():
    final_json = []
    data = client.service.Documents(10)
    courses = zeep.helpers.serialize_object(data)
    courses = courses['_raw_elements']

    for c in courses:
        aux = {}
        for info in c:
            tag = info.tag.split("}")
            aux[tag[1]] = info.text.strip()
        final_json.append(aux)
    return final_json

# courses = client.service.getcourses()
# print(type(courses))

# for e in courses:
#     for k in e:
#         print(type(k.text))
