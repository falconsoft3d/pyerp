#!/usr/bin/env python3
# Standard Library
from datetime import datetime

# Thirdparty Library
import eventlet
import requests
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('chat')
def message_chat(sid, message):
    # Registramos el mensaje
    print('\n\nentrando\n\n')
    res = requests.post('http://0.0.0.0:5000/chat/register_message', data={
        'sid': sid,
        'message': message,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    print('\n\n%s\n\n' % res.text)
    # Luego lo emitimos
    sio.emit('master', {
        'sid': sid,
        'message': message,
    })


@sio.on('chatr')
def message_response(sid, data):
    requests.post('http://0.0.0.0:5000/chat/register_message', data={
        'sid': data['sid'],
        'message': data['message'],
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'response': True
    })
    sio.emit('chat-%s' % data['sid'], data['message'])


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
