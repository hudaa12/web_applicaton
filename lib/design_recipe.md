{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

# Home route
GET /home
# sort-name route 
POST /sort-names

    names: list of names string format 

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# POST/ sort-names
# Paramters: 
#   names: Joe, Alice, Zoe, Julia, Kieran
# Expected response (200 OK):
"""
return the sorted list of names
Alice, Joe, Julia, Kieran, Zoe
"""



# POST /sort-names
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a list of names
"""


3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:




"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'



# POST/ sort-names
# Paramters: 
#   names: Joe, Alice, Zoe, Julia, Kieran
# Expected response (200 OK):
"""
return the sorted list of names
Alice, Joe, Julia, Kieran, Zoe
"""

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'name': ['Joe', 'Alice', 'Zoe', 'Julia', 'Kieran']})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'

# POST /sort-names
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a list of names
"""


def test_post_sort_names_none(web_client):
    with pytest.raises(Exception) as e:
        response = web_client.post('/sort-names', data=none)
    error_message = str(e.value)
    assert error_message == "Please provide a list of names"
    assert response.status_code == 400