# 


def find_k_terms(n):
    if n == 1 or n == 2:
        return [n]

    terms = list()
    part = 1
    while n-part > part:
        terms.append(part)
        n -= part
        part += 1
    terms.append(n)
    return(terms)


def main():
    # n = int(input())
    n = random.randint(1, 10000)
    func = find_k_terms(n)
    print(len(func))
    print(*func)


if __name__ == '__main__':
    main()
