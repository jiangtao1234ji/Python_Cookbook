# @Author  :_kerman jt
# @Time    : 19-7-29 下午1:08


from socket import socket, AF_INET, SOCK_STREAM
from functools import partial, total_ordering
import math
from abc import ABCMeta, abstractmethod
import collections
import bisect
import time
import operator
import types
import weakref


# class Pair:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Pair({self.x!r}, {self.y!r})'
#     def __str__(self):
#         return f'{self.x!s}, {self.y!s}'
#
# p = Pair(3,4)
# print(p)
# print(type(p))
# print(f'p is {p!r}')
# print(f'p is {p}')


# _formats = {
#     'ymd' : '{d.year}-{d.month}-{d.day}',
#     'mdy' : '{d.month}/{d.day}/{d.year}',
#     'dmy' : '{d.day}/{d.month}/{d.year}'
# }
#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def __format__(self, format_spec):
#         if format_spec == '':
#             format_spec = 'ymd'
#         fmt = _formats[format_spec]
#         return fmt.format(d=self)
# d = Date(2019,7,30)
# print(format(d))
# print(format(d,'mdy'))
# print(f'The date is {d:ymd}')
# print(f'The date is {d:mdy}')


# class LazyConnection:
#     def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
#         self.address =address
#         self.family = AF_INET
#         self.type = SOCK_STREAM
#         self.sock = None
#         #self.connections = []
#
#     def __enter__(self):
#         if self.sock is not None:
#             raise RuntimeError('Already connected')
#         self.sock = socket(self.family, self.type)
#         self.sock.connect(self.address)
#         #self.connections.append(sock)
#         return self.sock
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.sock.close()
#         self.sock = None
#         #self.connections.pop().close()
#
# conn = LazyConnection(('www.baidu.com', 80))
# with conn as s:
#     s.send(b'GET /index.thml HTTP/1.0\r\n')
#     s.send(b'Host: www.baidu.com\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv,8192), b''))


# class Date:
#     __slots__ = ['year', 'month', 'day']
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day


# class Person:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a String')
#         self._first_name = value
#
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")


# class A:
#     def spam(self):
#         print('A.spam')
#
# class B(A):
#     def spam(self):
#         print("B.spam")
#         super().spam()
# b = B()
# b.spam()


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Excepted a Srting')
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")
#
#
# class SubPerson(Person):
#     @property
#     def name(self):
#         print(("Getting name"))
#         return super().name
#
#     @name.setter
#     def name(self, value):
#         print(f"Setting name to {value}")
#         super(SubPerson, SubPerson).name.__set__(self, value)
#
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete(self)
#
#
# s = SubPerson('Gudio')
# print(s.name)
# s.name = 'Larry'
#
#
# class SubPerson(Person):
#     @Person.name.getter
#     def name(self):
#         print('Getting name')
#         return super().name
#
#
# class String:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise TypeError('Excepted a String')
#         instance.__dict__[self.name] = value
#
#
# class Person:
#     name = String('name')
#
#     def __init__(self, name):
#         self.name = name
#
#
# class SubPerson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name
#
#     @name.setter
#     def name(self, value):
#         print(f'Setting name to {value}')
#         super(SubPerson,SubPerson).name.__set__(self,value)
#
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete__(self)
#
# s = SubPerson('JT')


# class Integer:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError('Excepted a int')
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
# class Point:
#     x = Integer('x')
#     y = Integer('y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Point(2,3)
# print(p.x)
# p.y = 5
# print(p.y)
#
#
# class Typed:
#     def __init__(self, name, expected_type):
#         self.name = name
#         self.expected_type = expected_type
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.expected_type):
#             raise TypeError('Excepted ' + str(self.expected_type))
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
#
# def typeassert(**kwargs):
#     def decorate(cls):
#         for name, expected_type in kwargs.items():
#             setattr(cls, name, Typed(name, expected_type))
#         return cls
#     return decorate
#
# @typeassert(name=str, shares=int, price=float)
# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price


# class lazyproperty:
#     def __init__(self, func):
#         self.func = func
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance,self.func.__name__, value)
#             return value
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @lazyproperty
#     def area(self):
#         print('Computing area')
#         return math.pi * self.radius **2
#
#     @lazyproperty
#     def perimeter(self):
#         print('Computing perimeter')
#         return 2*math.pi*self.radius
#
# c = Circle(4.0)
# print(c.radius)
# print(c.area)


# class Structure:
#     _fields = []
#
#     def __init__(self, *args):
#         if len(args) != len(self._fields):
#             raise TypeError(f'Excepted {len(self._fields)} arguments')
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#
#
# class Stock(Structure):
#     _fields = ['name', 'shares', 'price']
#
#
# class Point(Structure):
#     _fields = ['x', 'y']
#
#
# class Circle(Structure):
#     _fields = ['radius']
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# print(Stock('ACME', 50, 91))


# class IStream(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self, maxbytes=-1):
#         pass
#     @abstractmethod
#     def write(self, data):
#         pass
#
# def serialize(obj, stream):
#     if not isinstance(stream, IStream):
#         raise TypeError('Excepted an IStream')
#
# class A(metaclass=ABCMeta):
#     @property
#     @abstractmethod
#     def name(self):
#         pass
#
#     @name.setter
#     @abstractmethod
#     def name(self, value):
#         pass
#
#     @classmethod
#     @abstractmethod
#     def method1(cls):
#         pass
#
#     @staticmethod
#     @abstractmethod
#     def method2():
#         pass


# class Descriptor:
#     def __init__(self, name=None, **opts):
#         self.name = name
#         for key, value in opts.items():
#             setattr(self, key, value)
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class Typed(Descriptor):
#     expected_type = type(None)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.expected_type):
#             raise TypeError('Expected' + str(self.expected_type))
#         super().__set__(instance, value)
#
#
# class Unsigned(Descriptor):
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Expected >= 0')
#         super().__set__(instance, value)
#
#
# class Maxsized(Descriptor):
#     def __init__(self, name=None, **opts):
#         if 'size' not in opts:
#             raise TypeError('missing size option')
#         super().__init__(name, **opts)
#
#     def __set__(self, instance, value):
#         if len(value) >= self.size:
#             raise ValueError('size must be < ' + str(self.size))
#         super().__set__(instance, value)
#
# class Integer(Typed):
#     expected_type = int
#
# class UnsignedInteger(Integer, Unsigned):
#     pass
#
# class Float(Typed):
#     expected_type = float
#
# class UnsignedFloat(Float, Unsigned):
#     pass
#
# class String(Typed):
#     expected_type = str
#
# class SizedString(String, Maxsized):
#     pass
#
# class Stock:
#     name = SizedString('name', size = 8)
#     shares = UnsignedInteger('shares')
#     price = UnsignedFloat('price')
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
# s = Stock('ACME', 50, 91.1)
# print(s.name)


# class SortedItems(collections.Sequence):
#     def __init__(self, initial=None):
#         self._items = sorted(initial) if initial is not None else []
#
#     def __getitem__(self, item):
#         return self._items[item]
#
#     def __len__(self):
#         return len(self._items)
#
#     def add(self, item):
#         bisect.insort(self._items, item)
#
# items = SortedItems([5,1,3])
# print(list(items))
# items.add(-2)
# print(list(items))


# class A:
#     def spam(self, x):
#         pass
#
#     def foo(self):
#         pass
#
# class B:
#     def __init__(self):
#         self._a = A()
#
#     def spam(self, x):
#         return self._a.spam(x)
#
#     def foo(self):
#         return self._a.foo()
#
#     def bar(self):
#         pass
#
# class C:
#     def __init__(self):
#         self._a = A()
#
#     def bar(self):
#         pass
#
#     def __getattr__(self, name):
#         return getattr(self._a, name)
#
# b = C()
# b.bar()
# print(b.spam(42))
#
#
# class Proxy:
#     def __init__(self, obj):
#         self._obj = obj
#
#     def __getattr__(self, item):
#         print('getattr:', item)
#         return getattr(self._obj, item)
#
#     def __setattr__(self, key, value):
#         if key.startswith('_'):
#             super().__setattr__(key, value)
#         else:
#             print('setattr', key, value)
#             setattr(self._obj, key, value)
#
#     def __delattr__(self, item):
#         if item.startswith('_'):
#             super().__delattr__(item)
#         else:
#             print('delattr:', item)
#             delattr(self._obj, item)
#
# class Spam:
#     def __init__(self, x):
#         self.x = x
#
#     def bar(self, y):
#         print('Spam.bar:', self.x, y)
#
# s = Spam(2)
# p = Proxy(s)
# print(p.x)
# p.bar(3)
# p.x = 33
# print(p.x)


# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def today(cls):
#         t = time.localtime()
#         return cls(t.tm_year, t.tm_mon, t.tm_mday)
#
#     def print(self):
#         print(self.year, self.month, self.day)
#
# a = Date(2019,8,2)
# b = Date.today()
# a.print()
# b.print()


# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
# d = Date.__new__(Date)
# print(d)
# #print(d.year)
# data = {'year':2019, 'month':8, 'day': 2}
# for key, value in data.items():
#     setattr(d, key, value)
# print(d.year)


# class LoggedMappingMixin:
#     __slots__ = ()
#
#     def __getitem__(self, item):
#         print('Getting ' + str(item))
#         return super().__getitem__(item)
#
#     def __setitem__(self, key, value):
#         print(f'Setting {key} = {value!r}')
#         return super().__setitem__(key,value)
#
#     def __delitem__(self, key):
#         print('Deleting ' + str(key))
#         return super().__delitem__(key)
#
# class SetOnceMappingMixin:
#     __slots__ = ()
#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + 'already set')
#         return super().__setitem__(key, value)
#
# class StringKeyMappingMixin:
#     __slots__ = ()
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError('keys must be strings')
#         return super().__setitem__(key, value)
#
# class LoggedDict(LoggedMappingMixin, dict):
#     pass
#
# d = LoggedDict()
# d['x'] = 23
# print(d['x'])
# del d['x']
#
#
# def LoggedMapping(cls):
#     cls_getitem = cls.__getitem__
#     cls_setitem = cls.__setitem__
#     cls_delitem = cls.__delitem__
#
#     def __getitem__(self, key):
#         print('Getting' + str(key))
#         return cls_getitem(self, key)
#
#     def __setitem__(self, key, value):
#         print(f'Setting {key} != {value!r}')
#         return cls_setitem(self, key, value)
#
#     def __delitem__(self, key):
#         print('Deleting ' + str(key))
#         return cls_delitem(self, key)
#
#     cls.__getitem__ = __getitem__
#     cls.__setitem__ = __setitem__
#     cls.__delitem__ = __delitem__
#     return cls
#
# @LoggedMapping
# class LoggedDict(dict):
#     pass


# class Connection:
#     def __init__(self):
#         self.state = 'Closed'
#
#     def read(self):
#         if self.state != 'Open':
#             raise RuntimeError('Not open')
#         print('reading')
#
#     def write(self, data):
#         if self.state != 'Open':
#             raise RuntimeError('Not open')
#         print('writing')
#
#     def open(self):
#         if self.state == 'Open':
#             raise RuntimeError('Already closed')
#         self.state = 'Closed'
#
# class Connection:
#     def __init__(self):
#         self.new_state(ClosedConnectionState)
#
#     def new_state(self, newstate):
#         self._state = newstate
#
#     def read(self):
#         return self._state.read(self)
#
#     def write(self, data):
#         return self._state.write(self, data)
#
#     def open(self):
#         return self._state.open(self)
#
#     def close(self):
#         return self._state.close(self)
#
# class ConnectionState:
#     @staticmethod
#     def read(conn):
#         raise NotImplementedError()
#
#     @staticmethod
#     def write(conn, data):
#         raise NotImplementedError()
#
#     @staticmethod
#     def open(conn):
#         raise NotImplementedError()
#
#     @staticmethod
#     def close(conn):
#         raise NotImplementedError()
#
# class ClosedConnectionState(Connection):
#     @staticmethod
#     def read(conn):
#         raise RuntimeError('Not open')
#
#     @staticmethod
#     def write(self, data):
#         raise RuntimeError('Not open')
#
#     @staticmethod
#     def open(conn):
#         conn.new_state(OpenConnectionState)
#
#     @staticmethod
#     def close(conn):
#         raise RuntimeError('Already closed')
#
# class OpenConnectionState(ConnectionState):
#     @staticmethod
#     def read(conn):
#         print('reading')
#
#     @staticmethod
#     def write(conn, data):
#         print('writing')
#
#     @staticmethod
#     def open(conn):
#         raise RuntimeError('Already open')
#
#     @staticmethod
#     def close(conn):
#         conn.new_state(ClosedConnectionState)
#
# c = Connection()
# print(c._state)
# c.open()
# c.read()
# c.write('hello world')
# c.close()


# class Point:
#     def __init__(self, x ,y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Point({self.x!r:},{self.y!r:})'
#
#     def distance(self, x, y):
#         return math.hypot(self.x-x, self.y-y)
#
# p = Point(2,3)
# d = getattr(p, 'distance')(0,0)
# print(d)
# print(p.distance(0,0))
# print(operator.methodcaller('distance', 0, 0)(p))
#
# points = [
#     Point(1,2),
#     Point(3,2),
#     Point(4,2),
#     Point(-2,2),
#     Point(21,-2)
# ]
# points.sort(key=operator.methodcaller('distance', 0, 0))


# class Node:
#     pass
#
# class UnaryOpeartor(Node):
#     def __init__(self, operand):
#         self.operand = operand
#
# class BinaryOperator(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
# class Add(BinaryOperator):
#     pass
#
# class Sub(BinaryOperator):
#     pass
#
# class Mul(BinaryOperator):
#     pass
#
# class Div(BinaryOperator):
#     pass
#
# class Negate(BinaryOperator):
#     pass
#
# class Number(Node):
#     def __init__(self, value):
#         self.value = value
#
# t1 = Sub(Number(3), Number(4))
# t2 = Mul(Number(2), t1)
# t3 = Div(t2, Number(5))
# t4 = Add(Number(1), t3)
#
# class NodeVisitor:
#     def visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#
#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
#
# class Evaluator(NodeVisitor):
#     def visit_Number(self, node):
#         return node.value
#
#     def visit_Add(self, node):
#         return self.visit(node.left) + self.visit(node.right)
#
#     def visit_Sub(self, node):
#         return self.visit(node.left) - self.visit(node.right)
#
#     def visit_Mul(self, node):
#         return self.visit(node.left) * self.visit(node.right)
#
#     def visit_Div(self, node):
#         return self.visit(node.left) / self.visit(node.right)
#
#     def visit_Negate(self, node):
#         return -node.operand
#
# e = Evaluator()
# print(e.visit(t4))
#
#
# class StackCode(NodeVisitor):
#     def generate_code(self, node):
#         self.instructions = []
#         self.visit(node)
#         return self.instructions
#
#     def visit_Number(self, node):
#         self.instructions.append(('PUSH', node.value))
#
#     def binop(self, node, instruction):
#         self.visit(node.left)
#         self.visit(node.right)
#         self.instructions.append((instruction,))
#
#     def visit_Add(self, node):
#         self.binop(node, 'ADD')
#
#     def visit_Sub(self, node):
#         self.binop(node, 'SUB')
#
#     def visit_Mul(self, node):
#         self.binop(node, 'MUL')
#
#     def visit_Div(self, node):
#         self.binop(node, 'DIV')
#
#     def unaryop(self, node, instrction):
#         self.visit(node.operand)
#         self.instructions.append((instrction,))
#
#     def visit_Negate(self, node):
#         self.unaryop(node, 'NEG')
#
# s = StackCode()
# s.generate_code(t4)



# class Node:
#     pass
#
#
# class NodeVisitor:
#     def visit(self, node):
#         stack = [node]
#         last_result = None
#         while stack:
#             try:
#                 last = stack[-1]
#                 if isinstance(last, types.GeneratorType):
#                     stack.append(last.send(last_result))
#                     last_result = None
#                 elif isinstance(last, Node):
#                     stack.append(self._visit(stack.pop()))
#                 else:
#                     last_result = stack.pop()
#             except StopIteration:
#                 stack.pop()
#         return last_result
#
#     def _visit(self, node):
#         methname = 'visit_' + type(node).__name__
#         meth = getattr(self, methname, None)
#         if meth is None:
#             meth = self.generic_visit
#         return meth(node)
#
#     def generic_visit(self, node):
#         raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
#
#
# class UnaryOpeartor(Node):
#     def __init__(self, operand):
#         self.operand = operand
#
#
# class BinaryOperator(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#
# class Add(BinaryOperator):
#     pass
#
#
# class Sub(BinaryOperator):
#     pass
#
#
# class Mul(BinaryOperator):
#     pass
#
#
# class Div(BinaryOperator):
#     pass
#
#
# class Negate(BinaryOperator):
#     pass
#
#
# class Number(Node):
#     def __init__(self, value):
#         self.value = value
#
#
# class Evaluator(NodeVisitor):
#     def visit_Number(self, node):
#         return node.value
#
#     def visit_Add(self, node):
#         yield (yield node.left) + (yield node.right)
#
#     def visit_Sub(self, node):
#         yield (yield node.left) - (yield node.right)
#
#     def visit_Mul(self, node):
#         yield (yield node.left) * (yield node.right)
#
#     def visit_Div(self, node):
#         yield (yield node.left) / (yield node.right)
#
#     def visit_Negate(self, node):
#         yield -(yield node.operand)



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self._parent = None
#         self.children = []
#
#     def __repr__(self):
#         return f'Node({self.value!r:})'
#
#     @property
#     def parent(self):
#         return self._parent if self._parent is None else self._parent()
#
#     @parent.setter
#     def parent(self, node):
#         self._parent = weakref.ref(node)
#
#     def add_child(self, child):
#         self.children.append(child)
#         child.parent = self
#
# root = Node('parent')
# c1 = Node('child')
# root.add_child(c1)
# print(c1.parent)
# del root
# print(c1.parent)


# class Room:
#     def __init__(self, name, length, width):
#         self.name = name
#         self.length = length
#         self.width = width
#         self.square_feet = self.length *self.width
#
# @total_ordering
# class House:
#     def __init__(self, name, style):
#         self.name = name
#         self.style = style
#         self.rooms = list()
#
#     @property
#     def living_space_footage(self):
#         return sum(r.square_feet for r in self.rooms)
#
#     def add_room(self, room):
#         self.rooms.append(room)
#
#     def __str__(self):
#         return f'{self.name}: {self.living_space_footage} squre foot {self.style}'
#
#     def __eq__(self, other):
#         return self.living_space_footage == other.living_space_footage
#
#     def __lt__(self, other):
#         self.living_space_footage < other.living_space_footage



class Spam:
    def __init__(self, name):
        self.name = name

_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

