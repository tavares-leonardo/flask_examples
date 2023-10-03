from flask import Flask

app = Flask(__name__)

names = []

@app.route('/')
def index():
    return 'Hello World!!!'

@app.route('/list')
def list():
    tmp = ''
    for name in names:
        tmp = tmp + name + '<br>'
    return tmp

@app.route('/insert/<name>')
def insert(name):
    names.append(name)
    return '{} inserted!'.format(name)

if __name__ == '__main__':
    app.run(debug=True)