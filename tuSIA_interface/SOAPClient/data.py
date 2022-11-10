import zeep
import json

wsdl = 'https://interfaceSOAPSIA2B.crvargasm.repl.co/wsdl?wsdl'
settings = zeep.Settings(strict=False, xml_huge_tree=True)
client = zeep.Client(wsdl=wsdl, settings=settings)


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
