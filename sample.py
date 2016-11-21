import math
import json
from graphics import GraphWin, Rectangle, Point


def area(cx, cy, r):
    return int(math.pi * r ** 2)


def inside(px, py, cx, cy, r):
    return r > ((cx - px)*2 + (cy - py)**2)**0.5


def half(cx, cy, r):
    return (cx, cy - r / 2, r / 2)


def mid(x, y, z):
    return sorted([x, y, z])[1]


def test_mid():
    return all([
        mid(0, 0, 0) is 0,
        mid(0, 0, 1) is 0,
        mid(0, 1, 0) is 0,
        mid(0, 1, 1) is 1,
        mid(1, 0, 0) is 0,
        mid(1, 0, 1) is 1,
        mid(1, 1, 0) is 1,
        mid(1, 1, 1) is 1,
        mid(0, 1, 2) is 1,
        mid(1, 2, 0) is 1,
        mid(1, 0, 2) is 1,
        mid(0, 2, 1) is 1,
        mid(2, 1, 0) is 1,
        mid(2, 0, 1) is 1
    ])


def nextrow(xs):
    return [i + j for i, j in zip([0] + xs, xs + [0])]


def pascal(n):
    array = [[1]]
    while n > len(array):
        array.append(nextrow(array[-1]))
    return array


def nomods(n, k):
    return 1


def everyk(xs, k):
    return 1


def square(n):
    return 1


def makeIndex(s):
    return 1


def before1st(x, s):
    return 1


def splitat2nd(x, s):
    return 1


def stairs(n):
    return 1


def noland(n):
    def draw(n):

        win = GraphWin('Noland', n, n)
        size = n / 3

        def partial(i, j, color):
            print(n, size, i, j, color)
            one = Point(i * size, j * size)
            two = Point(size * (i + 1), size * (j + 1))
            rect = Rectangle(one, two)
            rect.setFill(color)
            rect.setOutline(color)
            rect.draw(win)
            return rect
        return (win, partial)
    (win, partial) = draw(n)
    [partial(i, j, color) for i, row in enumerate([
        ['green', 'green', 'green'],
        ['green', 'red',    'blue'],
        ['green', 'blue',   'blue']
    ]) for j, color in enumerate(row)]
    win.getMouse()
    return True


print(json.dumps({
    '1': {
        'a': area(1, 1, 5) is 78,
        'b': inside(1, 1, 4, 4, 4),
        'c': half(4, 4, 4) == (4, 2, 2)
    },
    '2': {
        'a': mid(4, 6, 12) is 6,
        'b': test_mid()
    },
    '3': {
        'a': nextrow([1, 2, 1]) == [1, 3, 3, 1],
        'b': pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    },
    '4': {
        'a': nomods(10, 3) == [3, 6, 9],
        'b': everyk([3, 1, 4, 1, 5, 9], 2) == [3, 4, 5],
        'c': square(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    },
    '5': makeIndex('abba a-gog') == {
        'a': [0, 3, 5],
        'b': [1, 2],
        'g': [7, 9],
        '0': [8, 10],
        '-': [6],
        ' ': [4]
    },
    '6': {
        'a': before1st('l', 'Wales') == 'Wa',
        'b': splitat2nd('n', 'LyndonW') == ('Lyndo', 'W')
    },
    '7': stairs(4) is 5 and stairs(6) is 13,
    '8': noland(100)
}, sort_keys=True, indent=4))
