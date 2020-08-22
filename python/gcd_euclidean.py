# coding=utf-8

# find the greatest common divisor (GCD) of two int numbers
# https://en.wikipedia.org/wiki/Euclidean_algorithm

from pprint import pprint


def info(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result, int):
            pprint(dict(result=result))
        return func
    return wrapper


@info
def find_euclidean_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return find_euclidean_gcd(a % b, b)
    if b >= a:
        return find_euclidean_gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    a, b = 5545575, 246817485
    find_euclidean_gcd(a, b)


if __name__ == '__main__':
    main()
