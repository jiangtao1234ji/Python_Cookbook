__author__ = 'kerman jt'
# print(round(1.3333, 1), round(1.3353, 2), round(1.3333, 2), round(1.3333, 20))
# a = 1627731
# print(round(a, -1), round(a, -2), round(a, -3))
# x = 1.23456
# print(format(x, '0.2f'), format(x, '0.3f'))
# print('value is {:0.3f}'.format(x))


# from decimal import Decimal
# a = Decimal('2.11')
# b = Decimal('312.123')
# print((a+b))
# print((a+b) == Decimal('314.233'))


# b = 3 - 5j
# a = complex(2,4)
# print(a, b)
# print(a.real, a.imag, a.conjugate())


# a = float('inf')
# b = float('-inf')
# c = float('nan')
# import math
# print(a, b, c)
# print(math.isinf(a), math.isnan(c))
# print(a/a)
# print(a+b)
# d = float('nan')
# print(c == d, c is d)


# from fractions import Fraction
#
# a = Fraction(5, 4)
# b = Fraction(7, 16)
# print(a + b, a * b)
# c = a * b
# print(c.numerator, c.denominator)
# x = 3.75
# y = Fraction(*x.as_integer_ratio())
# print(y)


import numpy as np

# m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
# print(m)
# print(m.T)
# print(m.I)
# v = np.matrix([[2], [3], [4]])
# print(v)
# print(m * v)
"""行列式"""
# import numpy.linalg
# print(numpy.linalg.det(m))
"""特征值"""
# print(numpy.linalg.eigvals(m))
"""解x:   mx = v"""
# x = numpy.linalg.solve(m, v)
# print(x)


"""随机挑选元素"""
# import random
# values = [random.randint(0,40) for x in range(1000)]
# print(random.choices(values))
# print(random.sample(values, 10))
"""打乱顺序"""
# random.shuffle(values)
# print(values)
# print(random.getrandbits(100))


# from datetime import timedelta
#
# a = timedelta(days=2, hours=6)
# b = timedelta(hours=4.5)
# c = a + b
# print(c.days, c.seconds / 3600, c.total_seconds() / 3600)


# from datetime import datetime, timedelta
#
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Firday'
#     , 'Saturday', 'Sunday']
#
#
# def get_previous_byday(dayname, strat_date=None):
#     if strat_date is None:
#         strat_date = datetime.today()
#     day_num = strat_date.weekday()
#     day_num_target = weekdays.index(dayname)
#     day_ago = (7 + day_num - day_num_target) % 7
#     if day_ago == 0:
#         day_ago = 7
#     target_date = strat_date - timedelta(days=day_ago)
#     return target_date
#
#
# print(get_previous_byday('Monday'))
# print(get_previous_byday('Thursday'))
# print(get_previous_byday('Monday', datetime(2018, 12, 12)))
# from dateutil.relativedelta import relativedelta
# from dateutil.rrule import *
# d = datetime.now()
# print(d + relativedelta(weekday=FR))
# print(d + relativedelta(weekday=FR(-1)))


# from datetime import datetime, date, timedelta
# import calendar
#
#
# def get_month_range(start_date = None):
#     if start_date is None:
#         start_date = date.today().replace(day=1)
#     _,days_in_month = calendar.monthrange(start_date.year, start_date.month)
#     end_date = start_date + timedelta(days=days_in_month)
#     return (start_date, end_date)
# a_day = timedelta(days=1)
# first_day, last_day = get_month_range()
# while first_day < last_day:
#     print(first_day)
#     first_day += a_day
