# coding=utf-8

# check the correction of the brakets collection
# full task description: https://stepik.org/media/attachments/lesson/41233/statements.pdf

from pprint import pprint


def info(func):
    def wrapper(**kwargs):
        result = func(**kwargs)
        pprint(dict(func=func.__name__, result=result, kwargs=kwargs))
        return result
    return wrapper


@info
def stack(brackets):
    stack_chars = list()
    stack_idx = list()

    for idx, c in enumerate(brackets, start=1):
        if c in '([{':
            stack_chars.append(c)
            stack_idx.append(idx)

        elif c in ')]}':
            if not stack_chars:
                return idx

            top = stack_chars.pop()
            stack_idx.pop()

            if ((top == '(' and c != ')') or
                (top == '[' and c != ']') or
                (top == '{' and c != '}')):
                    return idx

    if stack_chars:
        print(stack_idx)
        return stack_idx.pop()

    return 'Success'


def main():
    assert stack(brackets='foo(bar[i);') == 10
    assert stack(brackets='{{{[][][]') == 3
    assert stack(brackets='[]([]') == 3
    assert stack(brackets=']]]') == 1
    assert stack(brackets='dasdsadsadas]]]') == 13
    assert stack(brackets='abc(()') == 4
    assert stack(brackets='{{{**[][][]') == 3
    assert stack(brackets='()[]}') == 5
    assert stack(brackets='{*{{}') == 3
    assert stack(brackets='{{[()]]') == 7
    assert stack(brackets='()[]}') == 5
    assert stack(brackets='[{[[[[[[[{}]]]]]]]}]') == 'Success'
    assert stack(brackets='()[]([])') == 'Success'
    assert stack(brackets=']([[[]]])') == 1
    assert stack(brackets='()[{[()]}]([())') == 15


if __name__ == '__main__':
    main()
