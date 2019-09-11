# @Author  :_kerman jt
# @Time    : 19-8-23 上午8:56


from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from urllib import request, parse
import requests
from http.client import HTTPConnection
from urllib import parse
from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, \
    ThreadingTCPServer, UDPServer, ThreadingUDPServer
from threading import Thread
import time
import ipaddress
import cgi
from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing.connection import Listener
import traceback
import pickle
import json
import hmac
import os
import ssl


# url = 'http://httpbin.org/get'
# parms = {
#     'name1' : 'value1',
#     'name2' : 'value2'
# }
# querystring = parse.urlencode(parms)
# u = request.urlopen(url + '?' + querystring)
# resp = u.read()
#
# u = request.urlopen(url, querystring.encode('ascii'))
# resp = u.read()
#
#
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam' : 'Eggs'
# }
#
# req = request.Request(url, querystring.encode('ascii'), headers=headers)
# u = request.urlopen(req)
# resp = u.read()
#
#
#
#
# url = 'http://httpbin.org/post'
# parms = {
#     'name1', 'value1',
#     'name2', 'value2'
# }
#
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
#
# resp = requests.post(url, data=parms, headers=headers)
#
# text = resp.text
#
# c = HTTPConnection('www.python.org', 80)
# c.request('HEAD', '/index.html')
# resp = c.getresponse()
# print('Status', resp.status)
# for name, value in resp.getheaders():
#     print(name, value)


# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print(f'Got connect from {self.client_address}')
#         while True:
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)
#
# serv = TCPServer(('', 20000), EchoHandler)
# serv.serve_forever()
#
# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         print(f'Got connect from {self.client_address}')
#         while True:
#             data = self.request.recv(1024)
#             if not data:
#                 break
#             print(data)
#             self.request.send(data)
#
#
# serv = TCPServer(('', 20001), EchoHandler)
# 多线程
# serv = ThreadingTCPServer(('', 20001), EchoHandler)
# serv.serve_forever()
#
#
# Networks = 16
# serv = TCPServer(('', 20000), EchoHandler)
# for n in range(Networks):
#     t = Thread(target=serv.serve_forever())
#     t.daemon = True
#     t.start()
# serv.serve_forever()
#
# serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
# serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# serv.server_bind()
# serv.server_activate()
# serv.serve_forever()
# 与上面实现相同功能
# TCPServer.allow_reuse_address = True
# serv = TCPServer(('', 20000), EchoHandler)
# serv.serve_forever()
#
#
# class EchoHandler(StreamRequestHandler):
#     timeout = 5
#     rbufsize = -1
#     wbufsize = 0
#     disable_nagle_algorithm = False
#     def handle(self):
#         print(f'Got connection from {self.client_address}')
#         try:
#             for line in self.rfile:
#                 self.wfile.write(line)
#         except socket.timeout:
#             print("Time out!")
#
# serv = TCPServer(('', 20001), EchoHandler)
# serv.serve_forever()
#
# def echo_handler(address, client_sock):
#     print(f'Got connect from {address}')
#     while True:
#         msg = client_sock.recv(8192)
#         if not msg:
#             break
#         client_sock.sendall(msg)
#     client_sock.close()
#
# def echo_server(address, backlog=5):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(address)
#     sock.listen(backlog)
#     while True:
#         client_sock, client_addr = sock.accept()
#         echo_handler(client_addr, client_sock)
#
# echo_server(('', 20000))


# class TimeHandler(BaseRequestHandler):
#     def handle(self):
#         print(f'Got connection from {self.client_address}')
#         msg, sock = self.request
#         resp = time.ctime()
#         sock.sendto(resp.encode('ascii'), self.client_address)
#
# serv = UDPServer(('', 20000), TimeHandler)
# serv.serve_forever()
# # 多进程
# serv = ThreadingUDPServer(('', 20000), TimeHandler)
# serv.serve_forever()
#
# def time_server(address):
#     sock = socket(AF_INET, SOCK_DGRAM)
#     sock.bind(address)
#     while True:
#         msg, addr = sock.recvfrom(8192)
#         print(f'Got message from {addr}')
#         resp = time.ctime()
#         sock.sendto(resp.encode('ascii'), addr)
#
# time_server(('', 20000))


# net = ipaddress.ip_network('123.44.50.64/27')
# print(net)
# for n in net:
#     print(n)
#
# net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
# print(net6)
# for n in net6:
#     print(n)
#
# print(net.num_addresses)
# print(net[0])
# ipaddress.ip_address('123.45.67.77')
# inet = ipaddress.ip_interface('123.45.67.73/27')
# print(inet.network)
# print(inet.ip)
#
# a = ipaddress.ip_address('127.0.0.1')
# s = socket(AF_INET, SOCK_STREAM)
# s.connect((str(a), 8080))


# def notfound_404(environ, start_response):
#     start_response('404 Not Found', [('Content-type', 'text/plain')])
#     return [b'Not Found']
#
# class PathDispatcher:
#     def __init__(self):
#         self.pathmap = {}
#
#     def __call__(self, environ, start_response):
#         path = environ['PATH_INFO']
#         params = cgi.FieldStorage(environ['wsgi.input'],
#                                   environ=environ)
#         method = environ['REQUEST_METHOD'].lower()
#         environ['params'] = {key : params.getvalue(key) for key in params}
#         handler = self.pathmap.get((method, path), notfound_404)
#         return handler(environ, start_response)
#
#     def register(self, method, path, function):
#         self.pathmap[method.lower(), path] = function
#         return function


# class KeyValueServer:
#     _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']
#
#     def __init__(self, address):
#         self._data = {}
#         self._serv = SimpleXMLRPCServer(address, allow_none=True)
#         for name in self._rpc_methods_:
#             self._serv.register_function(getattr(self, name))
#
#     def get(self, name):
#         return self._data[name]
#
#     def set(self, name, value):
#         self._data[name] = value
#
#     def delete(self, name):
#         del self._data[name]
#
#     def exists(self, name):
#         return name in self._data
#
#     def keys(self):
#         return list(self._data)
#
#     def serve_forever(self):
#         self._serv.serve_forever()
#
# kvserv = KeyValueServer(('', 15000))
# kvserv.serve_forever()


# def echo_client(conn):
#     try:
#         while True:
#             msg = conn.recv()
#             conn.send(msg)
#     except EOFError:
#         print('Connection closed')
#
# def echo_server(address, authkey):
#     serv = Listener(address, authkey=authkey)
#     while True:
#         try:
#             client = serv.accept()
#             echo_client(client)
#         except Exception:
#             traceback.print_exc()
# echo_server(('', 25000), authkey=b'peekaboo')




# class RPCHandler:
#
#     def __init__(self):
#         self._functions = {}
#
#     def register_function(self, func):
#         self._functions[func.__name__] = func
#
#     def handle_connection(self, connection):
#         try:
#             while True:
#                 func_name, args, kwargs = pickle.loads(connection.recv())
#                 try:
#                     r = self._functions[func_name](*args, **kwargs)
#                     connection.send(pickle.dumps(r))
#                 except Exception as e:
#                     connection.send(pickle.dumps(e))
#         except EOFError:
#             pass
#
#
# def rpc_server(handler, address, authkey):
#     sock = Listener(address, authkey=authkey)
#     while True:
#         client = sock.accept()
#         t = Thread(target=handler.handle_connection, args=(client,))
#         t.daemon = True
#         t.start()
#
#
# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# handler = RPCHandler()
# handler.register_function(add)
# handler.register_function(sub)
#
# rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')
#
#
# class RPCHandler:
#     def __init__(self):
#         self._functions = {}
#
#     def register_function(self, func):
#         self._functions[func.__name__] = func
#
#     def handle_connection(self, connection):
#         try:
#             while True:
#                 func_name, args, kwargs = json.loads(connection.recv())
#                 try:
#                     r = self._functions[func_name](*args, *kwargs)
#                     connection.send(json.dumps(r))
#                 except Exception as e:
#                     connection.send(json.dumps(str(e)))
#         except EOFError:
#             pass




# def server_authenticate(connection, secret_key):
#     message = os.urandom(32)
#     connection.send(message)
#     hash = hmac.new(secret_key, message)
#     digest = hash.digest()
#     response = connection.recv(len(digest))
#     return hmac.compare_digest(digest, response)
#
# secret_key = b"kerman"
#
# def echo_handler(client_sock):
#     if not server_authenticate(client_sock, secret_key):
#         client_sock.close()
#         return
#     while True:
#         msg = client_sock.recv(8192)
#         if not msg:
#             break
#         client_sock.sendall(msg)
#
# def echo_server(address):
#     s = socket(AF_INET, SOCK_STREAM)
#     s.bind(address)
#     s.listen(5)
#     while True:
#         c, a = s.accept()
#         echo_handler(c)
# echo_server(('', 18000))




KEYFILE = "server_key"
CERTFILE = "server_cert.pem"

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, )
