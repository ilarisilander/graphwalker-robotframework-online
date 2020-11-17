from flask import Flask, render_template

app = Flask(__name__)

data = 'default'

@app.route('/')
def index():
    global data
    print(data)
    return render_template("rest_index.html", data = data)

def get_data(step):
    global data
    data = step

if __name__ == "__main__":
    app.run(debug=True)
