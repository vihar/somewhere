from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/session',methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')


def messageRecived():
    print('message was received!!!')


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('recived my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
