__author__ = 'kerman jt'

import csv
from distributed.profile import process
from collections import namedtuple
import json
import pprint
from collections import OrderedDict
from xml.etree.ElementTree import iterparse, tostring
from xml.etree.ElementTree import Element
from struct import Struct
import struct


# csvfilename = ""
#
# with open(csvfilename) as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         #process(row)
#         pass

# with open(csvfilename) as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     Row = namedtuple('Row', headings)
#     for r in f_csv:
#         row = Row(*r)

# with open(csvfilename) as f:
#     f_csv = csv.DictReader(f)
#     for row in f_csv:
#         pass

# headers = []
# rows = []
# with open(csvfilename) as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)
#
# with open(csvfilename) as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(rows)


# s = '{"name" : "ACME", "shares" : 50, "price" : 490}'
# data = json.loads(s)
# print(json.dumps(data))
# print(json.dumps(data, indent=4))
# print(json.dumps(data,sort_keys=True))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Point(2,3)
# """无法实例化"""
# #json.dumps(p)
# def serialize_instance(obj):
#     d = {'__classname__' : type(obj).__name__}
#     d.update(vars(obj))
#     return d
#
# classes = {
#     'Point' : Point
# }
#
# def unserialize_object(d):
#     clsname = d.pop('__classname__', None)
#     if clsname:
#         cls = classes[clsname]
#         obj = cls.__new__(cls)
#         for key, value in d.items():
#             setattr(obj, key, value)
#         return obj
#     else:
#         return d
# s = json.dumps(p, default=serialize_instance)
# print(s)
# a = json.loads(s, object_hook=unserialize_object)
# print(a.y)


# def parse_and_remove(filename, path):
#     path_parts = path.split('/')
#     doc = iterparse(filename, ('start', 'end'))
#     next(doc)
#
#     tag_stack = []
#     elem_stack = []
#     for event, elem in doc:
#         if event == 'start':
#             tag_stack.append(elem.tag)
#             elem_stack.append(elem)
#         elif event == 'end':
#             if tag_stack == path_parts:
#                 yield elem
#                 elem_stack[-2].remove(elem)
#             try:
#                 tag_stack.pop()
#                 elem_stack.pop()
#             except IndexError:
#                 pass


# def dict_to_xml(tag, d):
#     elem = Element(tag)
#     for key, val in d.items():
#         child = Element(key)
#         child.text = str(val)
#         elem.append(child)
#     return elem
#
# s = {'name' : 'GOOG', 'shares': 100, 'price': 490}
# e = dict_to_xml('stock', s)
# print(tostring(e))
# e.set('id', '1111')
# print(tostring(e))


# def write_records(records, format, f):
#     record_struct = Struct(format)
#     for r in records:
#         f.write(record_struct.pack(*r))
#
#
# records = [(1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9)
#            ]
#
# with open('data.b', 'wb') as f:
#     write_records(records, '<idd', f)
#
# def read_records(format, f):
#     record_struct = Struct(format)
#     chunks = iter(lambda: f.read(record_struct.size), b'')
#     return (record_struct.unpack(chunk) for chunk in chunks)
#
# with open('data.b', 'rb') as f:
#     for rec in read_records('<idd', f):
#         print(rec)
#
# def unpack_records(format, data):
#     read_struct = Struct(format)
#     return (read_struct.unpack_from(data, offset)
#             for offset in range(0, len(data), read_struct.size))
#
# with open('data.b', 'rb') as f:
#     data = f.read()
#     for rec in unpack_records('<idd', data):
#         print(rec)


class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance.__buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self.__buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


class StructMeta(type):
    def __init__(self, clsname, bases, clsdict):
        fileds = getattr(self, '_fields_', [])
        byte_order = []
        offset = 0
        for format, filedname in fileds:
            if format.startswitch(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, filedname, StructField(format, offset))
            offset += struct.calcsize((format))
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructMeta):
    def __init__(self, bytedata):
        self.__buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fileds = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')

    ]


class NestedStruct:
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance.__buffer[self.offset:self.offset + self.struct_type.struct_size]
            result = self.struct_type(data)
            setattr(instance, self.name, result)
            return result


class StructMeta(type):
    def __init__(self, clsname, bases, clsdict):
        fileds = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fileds:
            if isinstance(format, StructMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswitch(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)

class Point(StructField):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]

class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),
        (Point, 'max'),
        ('i', 'num_polys')
    ]