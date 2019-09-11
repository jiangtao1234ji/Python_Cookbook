# @Author  :_kerman jt
# @Time    : 19-8-3 上午11:24


import time
from functools import wraps, partial
import logging
from inspect import signature, Signature, Parameter
import types
import inspect
from collections import OrderedDict
from abc import ABCMeta, abstractmethod
import operator
import sys
from contextlib import contextmanager
import ast
import dis
import opcode

# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper
#
# @timethis
# def countdown(n:int):
#     """
#     Count down
#     """
#     while n > 0:
#         n -= 1;
#
# countdown(100000)
# print(countdown.__name__, countdown.__doc__, countdown.__annotations__)


# def func1(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Func1')
#         return func(*args, **kwargs)
#     return wrapper
#
# def func2(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Func2')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @func1
# @func2
# def add(x, y):
#     return x + y
#
# print(add(2,3))
# print(add.__wrapped__(2,3))


# def logged(level, name=None, message=None):
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name__
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorate
#
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
#
# @logged(logging.CRITICAL, 'example')
# def spam():
#     print('Spam')
#
# print(add(3,2))
# spam()


# def attach_wrapper(obj, func=None):
#     if func is None:
#         return partial(attach_wrapper, obj)
#     setattr(obj, func.__name__, func)
#     return func
#
# def logged(level, name=None, message=None):
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name__
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#
#         @attach_wrapper(wrapper)
#         def set_level(newlevel):
#             nonlocal level
#             level = newlevel
#
#         @attach_wrapper(wrapper)
#         def set_message(newmsg):
#             nonlocal logmsg
#             logmsg = newmsg
#         return wrapper
#     return decorate
#
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
#
# @logged(logging.CRITICAL, 'example')
# def spam():
#     print('Spam!')
#
# logging.basicConfig(level=logging.DEBUG)
# print(add(2,3))
# add.set_message('All called')
# add(2,3)
# add.set_level(logging.WARNING)
# add(2,3)


# def logged(func=None,*,level=logging.DEBUG, name=None, message=None):
#     if func is None:
#         return partial(logged, level=level, name=name,message=message)
#     logname = name if name else func.__module__
#     log = logging.getLogger(logname)
#     logmsg = message if message else func.__name__
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         log.log(level, logmsg)
#         return func(*args, **kwargs)
#     return wrapper
#
# @logged
# def add(x, y):
#     return x + y
#
# @logged(level=logging.CRITICAL, name='example')
# def spam():
#     print('Spam!')


# def typeassert(*ty_args, **ty_kwargs):
#     def decorate(func):
#         if not __debug__:
#             return func
#         sig = signature(func)
#         bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             bound_values = sig.bind(*args, **kwargs)
#             for name, value in bound_values.arguments.items():
#                 if name in bound_types:
#                     if not isinstance(value, bound_types[name]):
#                         raise TypeError(
#                             f'Argument {name} must be {bound_types[name]}'
#                         )
#             return func(*args, **kwargs)
#         return wrapper
#     return decorate
# @typeassert(int, int)
# def add(x, y):
#     return x  + y
#
# print(add(2,3))
# # print(add(2,'2'))
#
# @typeassert(int, z=int)
# def spam(x, y, z=43):
#     print(x, y, z)
# spam(1,2,3)
# spam(1,'hello',3)


# class A:
#     def decorate1(self, func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print('decorate1')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     @classmethod
#     def decorate2(cls, func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print('decorate2')
#             return func(*args, **kwargs)
#         return wrapper
#
# a = A()
# @a.decorate1
# def spam():
#     pass
# @A.decorate2
# def grok():
#     pass
#
# class B(A):
#     @A.decorate2
#     def bar(self):
#         pass


# class Profiled:
#     def __init__(self, func):
#         wraps(func)(self)
#         self.ncalls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.ncalls += 1
#         return self.__wrapped__(*args, **kwargs)
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return types.MethodType(self, instance)
#
#
# @Profiled
# def add(x, y):
#     return x + y
#
#
# class Spam:
#     @Profiled
#     def bar(self, x):
#         print(self, x)
#
#
# print(add(2, 3))
# print(add.ncalls)
# print(add(2, 3))
# print(add.ncalls)
# s = Spam()
# s.bar(1)
# s.bar(1)
# s.bar(1)
# print(Spam.bar.ncalls)
#
#
# def profiled(func):
#     ncalls = 0
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         nonlocal ncalls
#         ncalls += 1
#         return func(*args, **kwargs)
#
#     wrapper.ncalls = lambda: ncalls
#     return wrapper
#
#
# @profiled
# def add(x, y):
#     return x + y
# print(add(2,3))
# print(add(3,3))
# print(add.ncalls())


# def optional_debug(func):
#     @wraps(func)
#     def wrapper(*args, debug=False, **kwargs):
#         if debug:
#             print('Calling', func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @optional_debug
# def spam(a, b, c):
#     print(a, b, c)
#
#
# spam(1, 23, 3)
# spam(1, 2, 3, debug=True)
#
#
# def optional_debug(func):
#     if 'debug' in inspect.getargspec(func).args:
#         raise TypeError('debug argumet already define')
#
#     @wraps(func)
#     def wrapper(*args, debug=False, **kwargs):
#         if debug:
#             print('Calling', func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def optional_debug(func):
#     if 'debug' in inspect.getargspec(func).args:
#         raise TypeError('debug argumet already define')
#
#     @wraps(func)
#     def wrapper(*args, debug=False, **kwargs):
#         if debug:
#             print('Calling', func.__name__)
#         return func(*args, **kwargs)
#
#     sig = inspect.signature(func)
#     parms = list(sig.parameters.values())
#     parms.append(inspect.Parameter('debug',
#                                    inspect.Parameter.KEYWORD_ONLY,
#                                    default=False))
#     wrapper.__signature__ = sig.replace(parameters=parms)
#     return wrapper
#
# @optional_debug
# def add(x, y):
#     return x + y
# print(inspect.signature(add))


# class NoInstance(type):
#     def __call__(self, *args, **kwargs):
#         raise TypeError("can't instantiate directly")
#
# class Spam(metaclass=NoInstance):
#     @staticmethod
#     def grok():
#         print('Spam.grok')
# Spam.grok()
# # s = Spam()
#
#
# class Singleton(type):
#     def __init__(self, *args, **kwargs):
#         self._instance = None
#         super().__init__(*args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         if self._instance is None:
#             self._instance = super().__call__(*args, **kwargs)
#             return self._instance
#         else:
#             return self._instance
#
# class Spam(metaclass=Singleton):
#     def __init__(self):
#         print('Creating Spam')
#
# a = Spam()
# b = Spam()
# print(b is a)


# class Typed:
#     _expected_type = type(None)
#
#     def __init__(self, name=None):
#         self._name = name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self._expected_type):
#             raise TypeError('Expected' + str(self._expected_type))
#         instance.__dict__[self._name] = value
#
#
# class Integer(Typed):
#     _expected_type = int
#
#
# class Float(Typed):
#     _expected_type = float
#
#
# class String(Typed):
#     _expected_type = str
#
#
# class OrderedMeta(type):
#     def __new__(cls, clsname, bases, clsdict):
#         d = dict(clsdict)
#         order = []
#         for name, value in clsdict.items():
#             if isinstance(value, Typed):
#                 value._name = name
#                 order.append(name)
#                 d['_order'] = order
#                 return type.__new__(cls, clsname, bases, d)
#
#     @classmethod
#     def __prepare__(cls, clsname, bases):
#         return OrderedDict()
#
#
# class Structure(metaclass=OrderedMeta):
#     def as_csv(self):
#         return ','.join(str(getattr(self, name)) for name in self._order)
#
#
# class Stock(Structure):
#     name = String()
#     shares = Integer()
#     price = Float()
#
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
#
# s = Stock('GOOD', 100, 290)
# print(s.as_csv())
#
#
# class NoDupOrderedDict(OrderedDict):
#     def __init__(self, clsname):
#         self.clsname = clsname
#         super().__init__()
#     def __setitem__(self, key, value):
#         if key in self:
#             raise TypeError(f'{key} already defined in {self.clsname}')
#         super().__setitem__(key,value)
#
#
# class OrderedMeta(type):
#     def __new__(cls, clsname, bases, clsdict):
#         d = dict(clsdict)
#         d['_order'] = [name for name in clsdict if name[0] != '_']
#         return type.__new__(cls, clsname, bases, d)
#
#     @classmethod
#     def __prepare__(cls, clsname, bases):
#         return NoDupOrderedDict(clsname)
#
# class A(metaclass=OrderedMeta):
#     def spam(self):
#         pass
#     def spam(self):
#         pass



# class IStream(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self, maxsize=None):
#         pass
#
#     @abstractmethod
#     def write(self, data):
#         pass
#
#
# class MyMeta(type):
#     @classmethod
#     def __prepare__(mcs, name, bases, *, debug=False, synchronize=False):
#         return super().__prepare__(name, bases)
#
#     def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
#         return super().__new__(cls, name, bases, ns)
#
#     def __init__(cls, name, bases, ns, *, debug=False, synchronize=False):
#         super().__init__(name, bases, ns)



# parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
#          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=423),
#          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
# sig = Signature(parms)
# print(sig)
#
# def func(*args, **kwargs):
#     bound_values = sig.bind(*args, **kwargs)
#     for name, value in bound_values.arguments.items():
#         print(name, value)
#
# func(1,23,z=3)
#
#
# def make_sig(*names):
#     parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
#              for name in names]
#     return Signature(parms)
#
# class Structure:
#     __signature__ = make_sig()
#     def __init__(self, *args, **kwargs):
#         bound_values = self.__signature__.bind(*args, **kwargs)
#         for name, value in bound_values.arguments.items():
#             setattr(self,name,value)
#
# class Stock(Structure):
#     __signature__ = make_sig('name', 'shares', 'price')
#
# class Point(Structure):
#     __signature__ =  make_sig('x', 'y')
#
# print(inspect.signature(Stock))
# s1 = Stock(('ACME'),12,1)
# s2 = Stock('ACME',121)
# s3 = Stock('ACME', 213,123,shares=22)
#
#
# class StructureMeta(type):
#     def __new__(cls, clsname, bases, clsdict):
#         clsdict['__signature__'] = make_sig(*clsdict.get('_fields',[]))
#         return super().__new__(cls, clsname, bases, clsdict)
#
# class Structure(StructureMeta):
#     _fields = []
#     def __init__(self, *args, **kwargs):
#         bound_values = self.__signature__.bind(*args, **kwargs)
#         for name, value in bound_values.arguments.items():
#             setattr(self,name,value)
#
# class Stock(Structure):
#     _fields = ['name', 'shares', 'price']
#
# class Point(Structure):
#     _fields = ['x', 'y']



# class MatchSignaturesMeta(type):
#     def __init__(self, clsname, bases, clsdict):
#         super().__init__(clsname, bases, clsdict)
#         sup = super(self, self)
#         for name, value in clsdict.items():
#             if name.startswith('_') or not callable(value):
#                 continue
#             prev_dfn = getattr(sup, name, None)
#             if prev_dfn:
#                 prev_sig = signature(prev_dfn)
#                 val_sig = signature(value)
#                 if prev_sig != val_sig:
#                     logging.warning(f'Signature mismatch in {value.__qualname__}. {prev_sig}'
#                                     f' != {val_sig}')
# class Root(metaclass=MatchSignaturesMeta):
#     pass
#
# class A(Root):
#     def foo(self, x ,y):
#         pass
#
#     def spam(self, x, *, z):
#         pass
#
# class B(A):
#     def foo(self, a, b):
#         pass
#
#     def spam(self, x, z):
#         pass




# def __init__(self, name, shares, price):
#     self.name = name
#     self.shares = shares
#     self.price = price
#
# def cost(self):
#     return self.shares * self.price
#
# cls_dict = {
#     '__init__': __init__,
#     'cost': cost,
# }
#
# Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
# Stock.__module__ = __name__
#
# s = Stock('ACME', 40, 33)
# print(s.cost())
#
#
#
# def named_tuple(classname, fieldnames):
#     cls_dict = {name: property(operator.itemgetter(n))
#                 for n, name in enumerate(fieldnames)}
#
#     def __new__(cls, *args):
#         if len(args) != len(fieldnames):
#             raise TypeError(f'Expected {len(fieldnames)} arguments')
#         return tuple.__new__(cls, args)
#     cls_dict['__new__'] = __new__
#     cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))
#     cls.__module__ = sys._getframe(1).f_globals['__name__']
#     return cls
#
# Point = named_tuple('Point', ['x','y'])
# p = Point(2,3)
# print(len(p))
# print(p.x, p.y)



# class StructTupleMeta(type):
#     def __init__(cls, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for n, name in enumerate(cls._fields):
#             setattr(cls, name, property(operator.itemgetter(n)))
#
# class StructTuple(tuple, metaclass=StructTupleMeta):
#     _fields = []
#     def __new__(cls, *args):
#         if len(args) != len(cls._fields):
#             raise ValueError(f'{len(cls._fields)} arguments requried')
#         return super().__new__(cls, args)
#
# class Stock(StructTuple):
#     _fields = ['name', 'shares', 'price']
#
# class Point(StructTuple):
#     _fields = ['x', 'y']
#
# s = Stock('ACME', 12, 122)
# print(s)
# print(s[0])
# print(s.name)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('name must be a string')
#         self._name = value
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int):
#             raise TypeError('age must be a int')
#         self._age = value
#
# def typed_property(name, expected_type):
#     storage_name = '_' + name
#
#     @property
#     def prop(self):
#         return getattr(self, storage_name)
#
#     @prop.setter
#     def prop(self, value, expected_type):
#         if not isinstance(value, expected_type):
#             raise TypeError(f'{name} must be a {expected_type}')
#         setattr(self, storage_name, value)
#     return prop
#
# class Person:
#     name = typed_property('name', str)
#     age = typed_property('age', int)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# String = partial(typed_property, expected_type=str)
# Integer = partial(typed_property, expected_type=int)
#
# class Person:
#     name = String('name')
#     age = Integer('age')
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age



# @contextmanager
# def timethis(label):
#     start = time.time()
#     try:
#         yield
#     finally:
#         end = time.time()
#         print(f'{label}: {end - start}')
#
# with timethis('counting'):
#     n = 10000000
#     while n > 0:
#         n -= 1
#
# @contextmanager
# def list_transaction(orig_list):
#     working = list(orig_list)
#     yield working
#     orig_list[:] = working
#
# items = [1,2,3]
# with list_transaction(items) as working:
#     working.append(4)
#     working.append(5)
#
# print(items)
# with list_transaction(items) as working:
#     working.append(6)
#     working.append(7)
#     raise RuntimeError('oops')
# print(items)



# def test():
#     a = 13
#     loc = locals()
#     exec('b = a + 1')
#     b = loc['b']
#     print(b)
# test()



# ex = ast.parse('2+3*4+x', mode='eval')
# print(ex)
# print(ast.dump(ex))
# top = ast.parse('for i in range(10): print(i)', mode='exec')
# print(top)
# print(ast.dump(top))
#
#
# class CodeAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.loaded = set()
#         self.stored = set()
#         self.deleted = set()
#
#     def visit_Name(self, node):
#         if isinstance(node.ctx, ast.Load):
#             self.loaded.add(node.id)
#         elif isinstance(node.ctx, ast.Store):
#             self.stored.add(node.id)
#         elif isinstance(node.ctx, ast.Del):
#             self.deleted.add(node.id)
#
# code = """
# for i in range(10):
#     print(i)
# del i"""
# top = ast.parse(code, mode='exec')
# c = CodeAnalyzer()
# c.visit(top)
# print(f'Loaded: {c.loaded}')
# print(f'Stored: {c.stored}')
# print(f'Delete: {c.deleted}')



# def countdown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#     print('Blastoff')
#
# print(dis.dis(countdown))
# c = countdown.__code__.co_code
# print(opcode.opname[c[0]])
#
# def generate_opcodes(codebytes):
#     extended_arg = 0
#     i = 0
#     n = len(codebytes)
#     while i < n:
#         op = codebytes[i]
#         i += 1
#         if op >= opcode.HAVE_ARGUMENT:
#             oparg = codebytes[i] + codebytes[i+1]*256 + extended_arg
#             extended_arg = 0
#             i += 2
#             if op == opcode.EXTENDED_ARG:
#                 extended_arg = oparg * 65536
#                 continue
#         else:
#             oparg = None
#         yield (op, oparg)
# for op, oparg in generate_opcodes(countdown.__code__.co_code):
#     print(op, opcode.opname[op], oparg)
#
# def add(x, y):
#     return x + y
#
# c = add.__code__
# print(c)
# print(c.co_code)
# newbytecode = b'xxxxxxx'
# nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount,
#                     c.co_nlocals, c.co_stacksize, c.co_flags, newbytecode,
#                     c.co_consts, c.co_names, c.co_varnames, c.co_filename,
#                     c.co_name, c.co_firstlineno, c.co_lnotab)
# print(nc)
# add.__code__ = nc
# add(2,3)