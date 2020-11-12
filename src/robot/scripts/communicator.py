from flask import Flask, render_template

app = Flask(__name__)
name = ''

@app.route('/')
def index():
    return render_template("rest_index.html", name = name)

def get_step_name(step):
    name = step
    print(step)

if __name__ == "__main__":
    app.run()
