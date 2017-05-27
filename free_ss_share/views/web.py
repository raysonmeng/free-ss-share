# coding=utf-8
from flask import Flask
from flask import render_template
from free_ss_share.utils.db_model import get
app = Flask(__name__)


@app.route('/')
def index():
    # print(get()[1])
    data = get()
    # for i in data:
    #     print i
    for i in data:
        print i
        i['location'] = i['location'].decode('utf-8')
    print data[1]

    # {
    #     'link': 'ss://Y2hhY2hhMjA6ZG91Yi5pbzMxNjU1QDEwNC4xNjAuMTczLjE0MTozMTY1NQ',
    #     'location': '美国 – 洛杉矶 2',
    #     'type': 'Shadowsocks',
    #     'update_time': '18:44:58'
    # }
    return render_template('index.html', data=data)


# @app.route('/admin')
# def admin():
#
#     return render_template('index.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
