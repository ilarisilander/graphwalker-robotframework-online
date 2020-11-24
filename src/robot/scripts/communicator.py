from flask import Flask, render_template, request
import requests, json

'''
This script is a communicator between getNext.py and index.html.
It receives information about the next step in a GraphWalker model,
and sends the information to index.html.

Start the Flask server by typing: python communicator.py in the terminal.
'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.get_json() # Get the request data from json
    if data != None: # Check if the data is empty
        print('From if')
        print(data['step'])
        return render_template("index.html", data = data['step']) # Send data to index.html which is in the templates folder
    else:
        print('From else')
        return render_template("index.html", data = '') # Send an empty string to index.html if the json data is "None"

if __name__ == "__main__":
    app.run(debug=True)
