# coding=utf-8

# cover each input segment with the minimum number of points

from pprint import pprint


def info(func):
    def wrapper(lines):
        result = func(lines)
        pprint(dict(result=result))
        return result
    return wrapper


@info
def find_min_points_set(lines):
    lines = sorted(lines, key=lambda x: (x[1], x[0]))
    points = set()
    point_crt = lines[0][1]
    points.add(point_crt)
    for line in lines[1:]:
        if line[0] > point_crt:
            point_crt = line[1]
            points.add(point_crt)
    return len(points), points


def main():
    # n = int(input())
    # lines = [list(map(int, input().split(' '))) for i in range(n)]
    lines = [[4, 7], [1, 3], [2, 5], [5, 6]]
    find_min_points_set(lines=lines)


if __name__ == '__main__':
    main()
