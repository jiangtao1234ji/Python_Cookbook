import time
from collections import defaultdict

__author__ = 'kerman jt'

# with open('/etc/passwd') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass
#
# with open('/etc/passwd') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')
# items = [1, 2, 3]
# it = iter(items)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return f'Node({self._value})'
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
# root = Node(0)
# child1 = Node(1)
# child2 = Node(2)
# root.add_child(child1)
# root.add_child(child2)
# for ch in root:
#     print(ch)


# def frange(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
# start = time.time()
# for n in frange(0, 10000000, 0.5):
#     a = n
# spend = (time.time() - start)
# print(spend)
# start = time.time()
# a = list(frange(0, 10000000, 0.5))
# spend = (time.time() - start)
# print(spend)
# start = time.time()
# a = [n for n in frange(0, 10000000, 0.5)]
# spend = (time.time() - start)
# print(spend)
# start = time.time()
# a = (n for n in frange(0, 1000000000, 1))
# spend = (time.time() - start)
# print(spend)
# def countdown(n):
#     print('Starting to count from', n)
#     while n > 0:
#         yield n
#         n -= 1
#     print('Done!')
#
# c = countdown(3)
# print(c)


# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._childern = []
#
#     def __repr__(self):
#         return f'Node({self._value})'
#
#     def add_child(self, node):
#         self._childern.append(node)
#
#     def __iter__(self):
#         return iter(self._childern)
#
#     def depth_first(self):
#         yield self
#         for c in self:
#             yield from c.depth_first()
#
#
# root = Node(0)
# child1 = Node(1)
# child2 = Node(2)
# root.add_child(child1)
# root.add_child(child2)
# child1.add_child(Node(3))
# child1.add_child(Node(4))
# child2.add_child(Node(5))
# for ch in root.depth_first():
#     print(ch)
#
#
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._childern = []
#
#     def __repr__(self):
#         return f'Node({self._value})'
#
#     def add_child(self, node):
#         self._childern.append(node)
#
#     def __iter__(self):
#         return iter(self._childern)
#
#     def depth_first(self):
#         return DepthFirstIterator(self)
#
#
# class DepthFirstIterator(object):
#     def __init__(self, start_node):
#         self._node = start_node
#         self._childern_iter = None
#         self._child_iter = None
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._childern_iter is None:
#             self._childern_iter = iter(self._node)
#             return self._node
#         elif self._child_iter:
#             try:
#                 nextchild = next(self._child_iter)
#                 return nextchild
#             except StopIteration:
#                 self._child_iter = None
#                 return next(self)
#         else:
#             self._child_iter = next(self._childern_iter).depth_first()
#             return next(self)
# root = Node(0)
# child1 = Node(1)
# child2 = Node(2)
# root.add_child(child1)
# root.add_child(child2)
# child1.add_child(Node(3))
# child1.add_child(Node(4))
# child2.add_child(Node(5))
# for ch in root.depth_first():
#     print(ch)


# a = [1, 2, 3, 4]
# for x in reversed(a):
#     print(x)
#
#
# class Countdown:
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#
#     def __reversed__(self):
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1
#
#
# from collections import deque
# class linehistory:
#     def __init__(self, lines, histlen=3):
#         self.lines = lines
#         self.history = deque(maxlen=histlen)
#
#     def __iter__(self):
#         for lineo, line in enumerate(self.lines, 1):
#             self.history.append(lineo, line)
#             yield line
#
#     def clear(self):
#         self.history.clear()


# def count(n: int) -> int:
#     while True:
#         yield n
#         n += 1
#
#
# c = count(0)
# import itertools
#
# for x in itertools.islice(c, 10, 20):
#     print(x)


# from itertools import dropwhile, islice
#
# with open('/etc/passwd') as f:
#     for line in dropwhile(lambda line: line.startswith('root'), f):
#         print(line, end='')
# items = ['a', 'b', 'c', 1, 4, 10, 15]
# for x in islice(items, 3, None):
#     print(x)
# items = ['a', 'b', 'c']
# from itertools import permutations
#
# for p in permutations(items):
#     print(p)
# for p in permutations(items, 2):
#     print(p)
# from itertools import combinations,combinations_with_replacement
# for c in combinations(items, 3):
#     print(c)
# for c in combinations(items, 2):
#     print(c)
# for c in combinations(items, 1):
#     print(c)
# for c in combinations_with_replacement(items, 3):
#     print(c)


# my_list = ['a', 'b', 'c']
# for idx, val in enumerate(my_list):
#     print(idx, val)
# for idx, val in enumerate(my_list, 1):
#     print(idx, val)
# def parse_data():
#     with open('/etc/passwd') as f:
#         for lineo, line in enumerate(f, 1):
#             fields = line.split()
#             try:
#                 count = int(fields[0])
#             except ValueError as e:
#                 print(f'Line {lineo}: Prase error: {e}')
# parse_data()
# word_summary = defaultdict(list)
# with open('/etc/passwd', 'r') as f:
#     lines = f.readlines()
# for idx,line in enumerate(lines):
#     words = [w.strip().lower() for w in line.split()]
#     for word in words:
#         word_summary[word].append(idx)
# print(word_summary)
#
# from itertools import zip_longest
# xpts = [1, 5, 4, 2, 10, 7]
# ypts = [101, 78, 37, 15, 62, 99]
# for x, y in zip(xpts, ypts):
#     print(x, y)
# xpts = [1, 5, 4, 2, 10, 7]
# ypts = [101, 78, 37, 15, 62]
# for x, y in zip(xpts, ypts):
#     print(x, y)
# for x, y in zip_longest(xpts, ypts):
#     print(x, y)
# for x, y in zip_longest(xpts, ypts, fillvalue=0):
#     print(x, y)
# print(zip(xpts, ypts))
# print(list(zip(xpts,ypts)))


# from itertools import chain
# a = [1,2,3,4]
# b = ['x', 'y', 'z']
# for x in chain(a,b):
#     print(x)


# import os
# import fnmatch
# import gzip
# import bz2
# import re
#
#
# def gen_find(filepat, top):
#     for path, dirlist, filelist in os.walk(top):
#         for name in fnmatch.filter(filelist, filepat):
#             yield os.path.join(path, name)
# def gen_opener(filenames):
#     for filename in filenames:
#         if filename.endswith('.gz'):
#             f = gzip.open(filename, 'rt')
#         elif filename.endswith('.bz2'):
#             f = bz2.open(filename, 'rt')
#         else:
#             f = open(filename, 'rt')
#         yield f
#         f.close()
#
# def gen_concatenate(iterators):
#     for it in iterators:
#         yield from it
#
# def gen_grep(pattern, lines):
#     pat = re.compile(pattern)
#     for line in lines:
#         if pat.search(line):
#             yield line
# lognames = gen_find('access-log*', 'www')
# files = gen_opener(lognames)
# lines = gen_concatenate(files)
# pylines = gen_grep('(?i)python', lines)
# for line in pylines:
#     print(line)
# bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
# bytes = (int(x) for x in bytecolumn if x != '-')
# print('Total', sum(bytes))


# from collections.abc import Iterable
# def flatten(items, ignore_types=(str, bytes)):
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x)
#         else:
#             yield x
# items = [1,2,[3,4,[5,6],7], 9]
# for x in flatten(items):
#     print(x)
# items = ['ax', 'bas', ['casd', 'dasf']]
# for x in flatten(items):
#     print(x)


# import heapq
# a = [2,8,3,4]
# b = [1,6,7,5]
# for c in heapq.merge(a, b):
#     print(c)


# CHUNKSIZE = 8192
# def reader(s):
#     while True:
#         data = s.recv(CHUNKSIZE)
#         if data == b'':
#             break
#         process_data(data)
#
# def reader(s):
#     for chunk in iter(lambda :s.recv(CHUNKSIZE), b''):
#         process_data(data)
import sys
f = open('/etc/passwd')
for chunk in iter(lambda : f.read(10), ''):
    n = sys.stdout.write(chunk)
