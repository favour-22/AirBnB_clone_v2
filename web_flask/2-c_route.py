from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['strict_slashes'] = False

@app.route('/', methods=['GET'])
def index():
    return "Hello HBNB!"

@app.route('/hbnb', methods=['GET'])
def hbnb():
    return "HBNB"

@app.route('/c/<text>', methods=['GET'])
def c(text):
    text = text.replace("_", " ")
    return "C " + text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
