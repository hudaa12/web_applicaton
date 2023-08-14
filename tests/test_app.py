# Tests for your routes go here
# """
# When: I make a GET request to /wave?name=Dana
# I expect the status code to be 200 OK
# and the response to be 'I am waving at Dana'
# """
# def test_get_wave(web_client):
#     response = web_client.get('/wave?name=Dana')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'I am waving at Dana'


# """
# When: I make a POST request to /submit
# And: I send a name and message as body parameters
# Then: I should get a 200 response with the right content
# """
# def test_post_submit(web_client):
#     response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'


"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'


"""
GET /home
Expected response (200 OK):
"This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'


"""
return the sorted list of names
Alice, Joe, Julia, Kieran, Zoe
"""

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe, Alice, Zoe, Julia, Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'
