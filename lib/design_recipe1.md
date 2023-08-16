{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

# add name route 
GET / names

    names: list of pre-defined names, plus the name given.

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE


# GET/ names?add=Eddie
# Paramters: 
#   names: Julia, Alice, Karim, Eddie
# Expected response (200 OK): 
"""
return the list of names
Julia, Alice, Karim, Eddie
"""


3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# GET/ names?add=Eddie
# Paramters: 
#   names: Julia, Alice, Karim, Eddie
# Expected response (200 OK):
"""
return the list of names
Julia, Alice, Karim, Eddie
"""

def test_get_names_no_add_param(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'


def test_get_names_with_add_param(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'
