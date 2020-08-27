# huffman incoder

from pprint import pprint


def info(func):
    def wrapper(**kwargs):
        result = func(**kwargs)
        pprint(dict(result=result))
        return result
    return wrapper


class TreeNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


def freq_counter(string):
    unique = ''.join(set(string))
    freq = [(lt, string.count(lt)) for lt in unique]
    freq = sorted(freq, key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:
        (lt_1, freq_1) = nodes.pop()
        (lt_2, freq_2) = nodes.pop()
        node = TreeNode(lt_1, lt_2)
        nodes.append((node, freq_1 + freq_2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    return nodes


@info
def huffman_coding(node, code=''):
    if isinstance(node, str):
        if code:
            return {node: code}
        else:
            return {node: '0'}

    left, right = node.children()
    d = dict()
    d.update(huffman_coding(node=left, code=code + '1'))
    d.update(huffman_coding(node=right, code=code + '0'))

    return d


def main():
    # string = str(input())
    string = 'abacabad'
    nodes = freq_counter(string=string)
    huffman = huffman_coding(node=nodes[0][0], code='')
    code = ''.join(huffman[lt] for lt in string)

    print(len(huffman), len(code))
    print(*(f"{lt}: {huffman[lt]}" for lt in huffman), sep='\n')
    print(code)


if __name__ == '__main__':
    main()
