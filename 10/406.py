# @Author  :_kerman jt
# @Time    : 19-8-13 下午10:52


import mymodule
from postimport import when_imported
import imp
import urllib.request
import sys


# a = mymodule.A()
# b = mymodule.B()
# a.spam()
# b.bar()
#
# math = importlib.import_module('math')
# print(math.sin(2))




# @when_imported('threading')
# def warn_threads(mod):
#     print('Thread? Are you crazy?')
#
# import threading



def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod

