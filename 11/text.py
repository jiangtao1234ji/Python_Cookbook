# @Author  :_kerman jt
# @Time    : 19-9-7 上午10:00
import hmac
import pickle
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from xmlrpc.client import ServerProxy
from multiprocessing.connection import Client
import json


# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 20000))
# s.send(b'Hello World!')
# print(s.recv(8192))


# s = socket(AF_INET, SOCK_DGRAM)
# s.connect(('localhost', 20000))
# s.send(b'Hello World!')
# print(s.recv(8192))


# s = ServerProxy('http://localhost:15000', allow_none=True)
# s.set('foo', 'bar')
# s.set('spam', [1,2,3])
# print(s.keys())
# print(s.get('foo'))
# print(s.get('spam'))
# s.delete('spam')
# print(s.exists('spam'))


# c = Client(('localhost', 25000), authkey=b'peekaboo')
# c.send('hello')
# print(c.recv())
# c.send(42)
# print(c.recv())
# c.send([1,2,3,4,5])
# print(c.recv())

# class RPCProxy:
#
#     def __init__(self, connection):
#         self._connection = connection
#
#     def __getattr__(self, name):
#         def do_rpc(*args, **kwargs):
#             self._connection.send(pickle.dumps((name, args, kwargs)))
#             result = pickle.loads(self._connection.recv())
#             if isinstance(result, Exception):
#                 raise result
#             return result
#
#         return do_rpc
#
#
# c = Client(('localhost', 17000), authkey=b'peekaboo')
# proxy = RPCProxy(c)
# print(proxy.add(2, 3))
# print(proxy.sub(2,3))
#
#
# class RPCProxy:
#     def __init__(self, connection):
#         self._connection = connection
#
#     def __getattr__(self, name):
#         def do_rpc(*args, **kwargs):
#             self._connection.send(json.dumps((name, args, kwargs)))
#             result = json.loads(self._connection.recv())
#             return result
#         return do_rpc


def client_authenticate(connection, secret_key):
    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)

secret_key = b"kerman"
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'Hello World')
resp = s.recv(1024)
print(resp)