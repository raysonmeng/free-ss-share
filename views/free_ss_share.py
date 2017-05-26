from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = 'asdasdasd'
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
