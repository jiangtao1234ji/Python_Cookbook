# @Author  :_kerman jt
# @Time    : 19-8-22 上午9:01

print("I am fib")

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) +  fib(n-2)

