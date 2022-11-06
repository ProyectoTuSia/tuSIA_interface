import zeep
import json

# wsdl = 'http://localhost:8000/server/getCourseById?wsdl'
# client = zeep.Client(wsdl=wsdl)


def getExternalCourses():
    # This function should return the xml raw structure

    data = {'id': "12920012-A",
            'nombre': "Calculo Diferencial",
            'creditos': 3,
            'tipologia': "Disciplinar Obligatoria",
            'sede': "Bogotá",
            'nivelestudio': "Maestría",
            'facultad': "Ingeniería",
            'descripcion': "Una materia más...",
            'prerequisitos': "Matemáticas Básicas, Inglés 1",
            'codigo': 12392312}
    return data
    # courses = client.service.getcourses()
    # print(type(courses))

    # for e in courses:
    #     for k in e:
    #         print(type(k.text))
