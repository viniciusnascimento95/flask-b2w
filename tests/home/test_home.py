import json


def test_index_response_200(client):

    response = client.get('/')

    # check status return 200
    assert response.status_code == 200
