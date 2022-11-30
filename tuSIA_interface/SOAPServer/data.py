import json
from gql import Client, gql
from gql.dsl import DSLSchema, DSLQuery, dsl_gql
from gql.transport.requests import RequestsHTTPTransport


transport = RequestsHTTPTransport(
    url="http://tusia-proxy-ag-service.default.svc.cluster.local/:80", verify=True, retries=3,)

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
