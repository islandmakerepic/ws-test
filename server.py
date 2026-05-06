from flask import Flask
from flask_sock import Sock
import time

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return 'OK'

@sock.route('/ws')
def websocket(ws):
    while True:
        message = ws.receive()
        ws.send(f"{message}|{time.time()}")

if __name__ == '__main__':
    app.run()
