import os
from flask import Flask, request, jsonify

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'


@app.route('/home', methods = ['GET'])
def get_home():
    return "This is my home page!"


@app.route('/sort-names', methods = ['POST'])
def post_sort_names():
    names = request.form['names'].split(',')
    sorted_names = sorted(names)
    return ','.join(sorted_names)



predefined_names = ['Julia', 'Alice', 'Karim']

@app.route('/names', methods=['GET'])
def get_names():
    add_name = request.args.get('add')
    if add_name:
        updated_names = predefined_names + [add_name]
        return ','.join(updated_names)
    else:
        return ','.join(predefined_names)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

