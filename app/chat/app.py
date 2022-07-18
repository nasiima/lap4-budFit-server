from flask import Flask;
from flask_cors import CORS
from flask_socketio import SocketIo, send

 chat =Flask(__name__)
 chat.config['SECRET_KEY']= "mysecret"
# chat = Blueprint('chat', __name__) 
# CORS(chat)

 socketIo = SocketIo(chat, cors_allowed_origins="*")

 app.debug

 app.host ="localhost"

 @socketIo.on("message")
 def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

if __name__ == "__main__":
    socketIo.run(app)
