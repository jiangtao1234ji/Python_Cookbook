import random

__author__ = 'kerman jt'

# 将序列分解为单独的变量
# p = (4, 5)
# x,y = p
# print(x)
# print(y)

# data = ['ACME', 50, 91.9, (2019, 5, 15)]
# name, shares, price, date = data
# print(name)
# name, shares, price, (year, mon, day) = data
# print(year, mon, day)

# def avg(data):
#     ans = 0
#     for i in data:
#         ans += i
#     return ans/len(data)
#
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)
#
#
# grades = [random.randint(80, 100) for i in range(1000000)]
# grades.sort()
# set(grades)
# print(drop_first_last(grades))

# records = [('foo', 1, 2),
#            ('bar', 'hello'),
#            ('foo', 3, 4)]
#
#
# def do_foo(x, y):
#     print('foo', x, y)
#
#
# def do_bar(s):
#     print('bar', s)
#
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     else:
#         do_bar(*args)
'''
foo 1 2
bar hello
foo 3 4'''

# from collections import deque
#
#
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
#
#
# if __name__ == '__main__':
#     with open('') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-' * 20)

# import heapq
#
# nums = [random.randint(-100,100) for i in range(1000)]
# print(heapq.nsmallest(3,nums))
# print(heapq.nlargest(3, nums))
# heap = list(nums)
# heapq.heapify(heap)
# print(max(heap))

# import heapq
#
#
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1
#
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
#
#
# class Item:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Item{{{self.name}}}"'
#
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('grok'), 1)
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())

# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d['a'])
#
# d = {}
# d.setdefault('a', []).append(1)
# print(d)
#
# d = {}
# pairs = {'runoob': 1, 'google': 2}
# for key, value in pairs.items():
#     if key not in d:
#         d[key] = []
#     d[key].append(value)
#
# d = defaultdict(list)
# for key, value in pairs.items():
#     d[key].append(value)
#
# from collections import OrderedDict
#
# d = OrderedDict()
# d['foo'] = 2
# d['bar'] = 1
# d['spam'] = 4
# d['grok'] = 3
# import json
# print(json.dumps(d))
"""dumps将dict转化为str"""

# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# price_sort = sorted(zip(prices.values(), prices.keys()))
# print(min(prices, key=lambda k:prices[k]))
# print(min_price)

# a = {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }
#
# b = {
#     'w': 10,
#     'x': 11,
#     'y': 2
# }
#
# print(a.keys() - b.keys())
# print(a.keys() & b.keys())
# print(a.items() & b.items())
# c = {key: a[key] for key in ((a.keys() | b.keys()) - (a.keys() ^ b.keys()))}
# print(c)

from collections import Hashable

#
# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
#
# print(list(dedupe([random.randint(0, 100) for k in range(1000)])))


# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
#
#
# a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
# list(dedupe(a, key=lambda d: (d['x'], d['y'])))
# list(dedupe(a, key=lambda d: d['x']))

# s = 'Helloworld'
# a = slice(2,4)
#
# print(a.indices(len(s)))

# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
#
# users = [User(23), User(3), User(100)]
# print(sorted(users, key=lambda u: u.user_id))
# from operator import attrgetter
# sorted(users, key=attrgetter('user_id'))


# nums = [random.randint(-100, 100) for k in range(10000)]
# """列表推导式"""
# ans1 = [n for n in nums if n > 0]
# """生成器表达式"""
# ans2 = (n for n in nums if n > 0)
# print(ans2)

# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
#
#
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
#
# ivals = list(filter(is_int, values))
# print(ivals)
# import math
# nums = [random.randint(-100, 100) for k in range(1000)]
# print([math.sqrt(int(n)) for n in ivals if int(n) > 0])
# clip_neg = [n if n > 0 else 0 for n in nums]
# print(clip_neg)

# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# p1 = {key:value for key, value in prices.items() if value > 100}
# print(p1)
# p2 = dict((key, value) for key, value in prices.items() if value > 100)
# print(p2)


# from collections import namedtuple
#
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2019-5-16')
# print(sub, sub.addr, sub.joined)
#
#
# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         total += rec[1] * rec[2]
#     return total
#
# Stock = namedtuple('Stock', ['name', 'shares', 'price'])
# def name_compute_cost(records):
#     total = 0.0
#     for rec in records:
#         s = Stock(*rec)
#         total += s.shares * s.price
#     return total
#
# s = Stock('ACME', 100, 123.45)
# print(s)
# s = s._replace(shares=75)
# print(s)


# nums = [random.randint(-100, 100) for k in range(1000)]
# s = sum(x * x for x in nums)
# print(s)
# s = sum([x * x for x in nums])
# print(s)

from collections import ChainMap
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values, values['x'])
values = values.parents
print(values, values['x'])
values = values.parents
print(values, values['x'])
