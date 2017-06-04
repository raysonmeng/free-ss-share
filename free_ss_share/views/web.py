# coding=utf-8
from flask import Flask
from flask import render_template

from free_ss_share.db.redis_model import get

app = Flask(__name__)


@app.route('/')
def index():
    data = get()
    for i in data:
        i['location'] = i['location'].decode('utf-8')
    return render_template('index.html', data=sorted(data, key='score')[::-1])


# @app.route('/admin')
# def admin():
#
#     return render_template('index.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
