from flask import Flask
from flask import request
import netifaces


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/clientip")
def clientip():
    return 'Hi, %r, this is %s' % (
        request.headers.get('X-Forwarded-For'),
        netifaces.ifaddresses('eth0')[2][0]['addr'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
