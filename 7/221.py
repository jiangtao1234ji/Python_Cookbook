# @Author  :_kerman jt
# @Time    : 19-7-28 下午8:49

from functools import partial
from urllib.request import urlopen
from queue import Queue
from functools import wraps
import sys
from timeit import timeit


# def avg(first, *rest):
#     return (first + sum(rest)) / (1 + len(rest))
#
#
# print(avg(1, 2, 3, 4, 5))
#
#
# def recv(maxsize, *, block):
#     pass
#
#
# # recv(1024,True) #wrong
# recv(1024, block=True)


# def add(x: int, y: int) -> int:
#     return x + y
# print(add.__annotations__)


# def spam(a, b=42):
#     print(a, b)
#
#
# spam(1)
# spam(1, 2)
#
#
# def spam(a, b=None):
#     if b is None:
#         b = []
#
#
# no_value = object()
#
#
# def spam(a, b=no_value):
#     if b is no_value:
#         print('No b value supplied')


# x = 10
# a = lambda y: x + y
# x = 20
# b = lambda y: x + y
# print(a(10),b(10))
#
# x = 10
# a = lambda y, x=x: x + y
# x = 20
# b = lambda y, x=x: x + y
# print(a(10),b(10))


# def spam(a,b,c,d):
#     print(a,b,c,d)
#
# s1 = partial(spam,1)
# s1(3,4,1)
# s2 = partial(spam, d = 22)
# s2(3,4,1)
# s3 = partial(spam, 1,d=21)
# s3(234,231)


# 闭包
# def urltemplate(template):
#     def opener(**kwargs):
#         return urlopen(template.format_map(kwargs))
#     return opener


#ps(注意args 和　*args的区别)
# def apply_async(func, args, callback):
#     result = func(*args)
#     callback(result)
#
#
# def print_result(result):
#     print('Got:', result)
#
#
# def add(x, y):
#     return x + y
#
#
# apply_async(add, (2, 3), callback=print_result)
# apply_async(add, ('hello', 'world'), callback=print_result)
#
# class ResultHandler:
#     def __init__(self):
#         self.sequence = 0
#     def handler(self, result):
#         self.sequence += 1
#         print(f'[{self.sequence}] Got: {result}')
#
#
# def make_handler():
#     sequence = 0
#     def handler(result):
#         nonlocal sequence
#         sequence += 1
#         print(f'[{sequence}] Got: {result}')
#     return handler
#
# def xiechen_handler():
#     sequence = 0
#     while True:
#         result = yield
#         sequence += 1
#         print(f'[{sequence}] Got: {result}')
#
#
# r = ResultHandler()
# handler = make_handler()
# x = xiechen_handler()
# next(x)
# apply_async(add,(2,3),callback=r.handler)
# apply_async(add,2,3,callback=r.handler)
# apply_async(add,2,3,callback=handler)
# apply_async(add,2,3,callback=handler)
# apply_async(add,2,3,callback=x.send)
# apply_async(add,2,3,callback=x.send)


# def apply_async(func, args, *, callback):
#     result = func(*args)
#     callback(result)
#
#
# class Async:
#     def __init__(self, func, args):
#         self.func = func
#         self.args = args
#
#
# def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#         f = func(*args)
#         result_queue = Queue()
#         result_queue.put(None)
#         while True:
#             result = result_queue.get()
#             try:
#                 a = f.send(result)
#                 apply_async(a.func, a.args, callback=result_queue.put)
#             except StopIteration:
#                 break
#
#     return wrapper
#
# def add(x,y):
#     return x+y
#
# @inlined_async
# def test():
#     r = yield Async(add, (2,3))
#     print(r)
#
# test()


class ClosureInstance:
    def __init__(self, locals = None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


s1 = Stack()
s2 = Stack2()
print(timeit('s1.push(1);s1.pop()', 'from __main__ import s1',number=1000000))
print(timeit('s2.push(1);s2.pop()','from __main__ import s2',number=1000000))