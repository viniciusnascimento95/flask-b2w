# import json

# def test_home_response_hello(client):
#     response = client.get('/')

#     data = json.loads(response.data.decode('utf-8'))

#     assert data['hello'] == 'world by apps'