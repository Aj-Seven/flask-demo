from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Aj7!!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!!"

@app.route('/about')
def about():
    return "Simple Flask Test"

if __name__ == "__main__":
    app.run(debug=True)
