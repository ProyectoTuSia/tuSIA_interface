import json
from gql import Client, gql
from gql.dsl import DSLSchema, DSLQuery, dsl_gql
from gql.transport.requests import RequestsHTTPTransport
import os

pem_path = os.path.basename('key.pem')
transport = RequestsHTTPTransport(
    url="https://tusia-proxy-https-ag-service.default.svc.cluster.local:443", verify=False, retries=3,)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Standard GraphQL query


def getAllCourses():
    query = gql(
        """
query GetSubject {
  getSubject {
    Id_subject
    Name_subject
    Credits
    Description
  }
}

"""


    )

    data = client.execute(query)
    data = data['getSubject']
    # print(data)
    print(type(data))

    return data


# Execute query and normalize the json response payload

# prjs.head()
