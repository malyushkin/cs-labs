# coding=utf-8
#
# find the n-th number of the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ..., F(n) = F(n-1) + F(n-2)

from pprint import pprint


def memoize(func):
    cache = dict()

    def wrapper(n, *args):
        if n not in cache:
            cache[n] = func(n)
            pprint(dict(func=func.__name__, result=cache[n], n=n, args=args))
        return cache[n]
    return wrapper


@memoize
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


@memoize
def fib_arr(n):
    f0, f1 = 0, 1
    for i in range(1, n):
        f0, f1 = f1, f0 + f1
    return f1


def main():
    fib_recursive(15)
    fib_arr(20)


if __name__ == '__main__':
    main()
