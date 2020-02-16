# алгоритм Хаффмана

from collections import deque, Counter, namedtuple
import heapq


class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, seq, bit):
        self.left.walk(seq, bit + '0')
        self.right.walk(seq, bit + '1')


class Leaf(namedtuple('Leaf', ['char'])):

    def walk(self, seq, bit):
        seq[self.char] = bit or '0'


def huffman_code(str):
    hq = []
    for char, freq in Counter(str).items():
        hq.append((freq, len(hq), Leaf(char)))
    heapq.heapify(hq)
    count = len(hq)
    while len(hq) > 1:
        freq_1, _count_1, left = heapq.heappop(hq)
        freq_2, _count_2, right = heapq.heappop(hq)
        heapq.heappush(hq, (freq_1 + freq_2, count, Node(left, right)))
        count += 1

    ch_code = {}
    [(_freq, _count, root)] = hq

    root.walk(ch_code, '')

    return ch_code


str = input('Введте строку для кодирования: \n')
code = huffman_code(str)
encoded = ''.join(code[char] for char in str)
print('Закодированная строка: \n', encoded)
print('словарь кодирования символов: \n', *sorted(code))
