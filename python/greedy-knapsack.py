# coding=utf=8

from pprint import pprint


def info(func):
    def wrapper(*args):
        result = func(*args)
        pprint(dict(result=result, args=args))
        return result
    return wrapper


@info
def fill_knapsack(items, w):
    items = [(p / c, c) for p, c in items]
    items.sort(reverse=False)
    total = 0

    while w and items:
        per_kilo, capacity = items.pop()
        take = min(w, capacity)
        total += per_kilo * take
        w -= take

    return total


def main():
	n, w = map(int, input().split())
	items = [list(map(int, input().split(' '))) for i in range(n)]
	# n, w = 5, 50
	# items = [[60, 20], [100, 50], [120, 30]]
	print(fill_knapsack(items, w))
  
    
if __name__ == '__main__':
    main()
