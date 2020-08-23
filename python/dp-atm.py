# using the available nominal banknotes at the ATM `n1, n2, ..., nm`, get an amount of N rubles using the minimum number of banknotes, or inform that the requested cannot be dispensed. Stocks of banknotes of each denomination are unlimited


from pprint import pprint


def info(func):
    def wrapper(**kwargs):
        result = func(**kwargs)
        pprint(dict(result=result, args=kwargs))
        return result
    return wrapper


@info
def get_banknotes(amount, banknotes):
    cnts = [0 for i in range(amount+1)]
    outputs = {i: [] for i in range(amount+1)}
    n = len(banknotes)

    if amount < min(banknotes):
        return 'NaN'

    # O (N*M), N — sum amount, M — banknotes count 
    for i in range(min(banknotes), amount+1):
        smallest = float('inf')
        for j in range(0, n):
            if (banknotes[j] <= i):
                smallest = min(smallest, cnts[i - banknotes[j]])
                if smallest == cnts[i - banknotes[j]]:
                    outputs[i] = [banknotes[j]] + outputs[i-banknotes[j]]
        cnts[i] = 1 + smallest
    
    return sorted(outputs[amount])


def main():
    assert get_banknotes(amount=120, banknotes=[100, 60, 10]) == sorted([60, 60])
    assert get_banknotes(amount=130, banknotes=[100, 60, 10]) == sorted([10, 60, 60])
    assert get_banknotes(amount=160, banknotes=[100, 60, 10]) == sorted([100, 60])
    assert get_banknotes(amount=180, banknotes=[100, 60, 10]) == sorted([60, 60, 60])
    assert get_banknotes(amount=400, banknotes=[90, 60, 10, 80]) == sorted([80, 80, 80, 80, 80])
    assert get_banknotes(amount=50, banknotes=[100, 200]) == 'NaN'


if __name__ == '__main__':
    main()
