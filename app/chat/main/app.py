from flask import Flask, flask;
from flask_socketio import SocketIO, send
import socketio 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretKey'

socketIo = SocketIO(app, cors_allowed_origins='*')

app.debug = True

app.host = 'localhost'


@socketio.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None

if __name__ == '__main__':
    socketIo.run(app)