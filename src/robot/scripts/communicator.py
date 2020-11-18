from flask import Flask, render_template

'''
This script is a communicator between getNext.py and index.html.
It receives information about the next step in a GraphWalker model,
and sends the information to index.html.
'''

app = Flask(__name__)

data = 'default'

@app.route('/')
def index():
    global data
    print(data)
    return render_template("index.html", data = data)

def get_data(step):
    global data
    data = step

if __name__ == "__main__":
    app.run(debug=True)
