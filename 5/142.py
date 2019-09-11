import io
import os
import time

__author__ = 'kerman jt'
# import sys
# print(sys.getdefaultencoding())
"""输出重定向到文件中"""
# with open('xxx', 'rt') as f:
#     print('Hello World!', file=f)


# print('ACME', 40, 2321)
# print('ACME', 40, 2321, sep=',')
# print('ACME', 40, 2321, sep=',', end='!!\n')
# row = ('ACME', 3, 23)
# print(','.join(str(x) for x in row))
# print(*row, sep=',')


# t = 'Hello World!'
# for c in t:
#     print(c)
# b = b'Hellow World!'
# for c in b:
#     print(c)


# s = io.StringIO()
# print(s.write('Hello World\n'))
# print('This is a test', file=s)
# print(s.getvalue())
# s = io.StringIO('Hello\nWorld\n')
# print(s.read(4))
# print(s.read())
# s = io.BytesIO()
# s.write(b'binary data')
# print(s.getvalue())


# import gzip, bz2
# with gzip.open('','rt') as f:
#     text = f.read()
# with bz2.open('','rt') as f:
#     text = f.read()
# with gzip.open('','wt') as f:
#     f.write(text)
# with bz2.open('','wt') as f:
#     f.write(text)
# f = open('','rb')
# with gzip.open(f, 'rt') as f:
#     text = f.read()


# from functools import partial
# RECORD_SIZE = 32
# with open('','rb') as f:
#     records = iter(partial(f.read, RECORD_SIZE), b'')
#     for r in records:


# import os.path
# def read_into_buffer(filename):
#     buf = bytearray(os.path.getsize(filename))
#     with open(filename, 'rb') as f:
#         f.readinto(buf)
#     return buf
# with open('sample.bin', 'wb') as f:
#     f.write(b'Hello World')
# buf = read_into_buffer('sample.bin')
# print(buf)
# buf[0:5] = b'Hallo'
# print(buf)
# m1 = memoryview(buf)
# m2 = m1[-5:]
# print(m2)
# m2[2:] = b'RlD'
# print(buf)


# import mmap
# def memory_map(filename, access=mmap.ACCESS_WRITE):
#     size = os.path.getsize(filename)
#     fd = os.open(filename, os.O_RDWR)
#     return mmap.mmap(fd,size,access=access)
# size = 100000
# with open('data', 'wb') as f:
#     f.seek(size-1)
#     f.write(b'\x00')
# m = memory_map('data')
# print(len(m), m[0:10], m[0])
# m[0:11] = b'Hello World'
# m.close()
# with open('data', 'rb') as f:
#     print(f.read(11))


# path = '/Users/aa/as/data.csv'
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.join('tmp', 'data', os.path.basename(path)))
# path = '~/as/data.csv'
# print(os.path.expanduser(path))
# print(os.path.split(path))


# print(os.path.exists('/etc'))
# print(os.path.isfile('/etc'), os.path.isdir('/etc'))
# print(os.path.getsize('/etc/passwd'))
# print(os.path.getmtime('/etc/passwd'))
# print(time.ctime(os.path.getmtime('/etc/passwd')))


# names = [name for name in os.listdir('/etc')
#          if os.path.isfile(os.path.join('/etc', name))]
# dirnames = [name for name in os.listdir('/etc')
#             if os.path.isdir(os.path.join('/etc', name))]
# pyfile = [name for name in os.listdir('/etc')
#           if name.endswith('.py')]
# import glob
#
# pyfiles = glob.glob('/etc/*.py')
# from fnmatch import fnmatch
#
# pyfiles = [name for name in os.listdir('/etc')
#            if fnmatch(name, '*.py')]
# pyfiles = glob.glob('*.py')
# name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
#                 for name in pyfiles]
# for name, size, mtime in name_sz_date:
#     print(name, size, mtime)
# file_metdata = [(name, os.stat(name)) for name in pyfiles]
# for name, meta in file_metdata:
#     print(name, meta.st_size, meta.st_mtime)


# from socket import socket, AF_INET, SOCK_STREAM
# def echo_client(client_sock, addr):
#     print('Got connection from', addr)
#     client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
#     client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)
#     for line in client_in:
#         client_out.write(line)
#         client_out.flush()
#     client_sock.close()
# def echo_server(address):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(address)
#     socket.listen(1)
#     while True:
#         client, addr = sock.accept()
#         echo_client(client, addr)


# from tempfile import TemporaryFile
# with TemporaryFile('w+t') as f:
#     f.write('Hello World\n')
#     f.write('Testing\n')
#     f.seek(0)
#     data = f.read()


# import pickle
# data = [1,1,1,1,1]
# f = open('data', 'wb')
# pickle.dump(data,f)
# s = pickle.dumps(data)
import time, threading


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


c = Countdown(30)
