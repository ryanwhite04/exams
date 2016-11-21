import math
import json


def circumference(cx, cy, r):
    return 2 * math.pi * r


def origin(cx, cy, r):
    return r > (cx**2 + cy**2)**(1/2)


def biggest(px, py, cx, cy, r):
    return (px, py, r - int(((cx - px)**2 + (cy - py)**2)**0.5))


def fits(b1, b2, x):
    return x is len([b for b in [b1, b2] if b])


def test_fits():
    return all([
        fits(False, False, 0),
        not fits(False, False, 1),
        not fits(False, True,  0),
        fits(False, True,  1),
        not fits(True,  False, 0),
        fits(True,  False, 1),
        not fits(True,  True,  0),
        not fits(True,  True,  1),
    ])


def zipper(xs, ys):
    return [i for pair in zip(xs, ys) for i in pair]


def cumulative(xs):
    sum = 0
    cum = []
    for i in xs:
        sum += i
        cum.append(sum)
    return cum


def between(x, y):
    return [i for i in range(x, y + 1, x) if not y % i]


def pairs(n):
    return [(i, j) for i in range(n) for j in range(n) if 0 <= i < j < n]


def uncompress(xs):
    array = []
    first = True
    for i in xs:
        array += i * [first]
        first = not first
    return array


def palindrome(xs):
    return xs == xs[::-1]


def loseprefix(xs):
    first = xs[0]
    while first == xs[0]:
        xs = xs[1:]
    return xs


def substrings(xs):
    return [xs[j:i] for i in range(len(xs) + 1) for j in range(i)]


print(json.dumps({
    '1': {
        'a': int(circumference(4, -4, 4)) is 25,
        'b': origin(3, 4, 6),
        'c': biggest(5, 5, 1, 2, 9) == (5, 5, 4)
    },
    '2': {
        'a': fits(False, True, 1),
        'b': test_fits() is True
    },
    '3': {
        'a': zipper([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6],
        'b': cumulative([9, 7, -2, 4, 0, -1]) == [9, 16, 14, 18, 18, 17]
    },
    '4': {
        'a': between(3, 18) == [3, 6, 9, 18],
        'b': pairs(4) == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)],
    },
    '5': uncompress([2, 1, 1]) == [True, True, False, True],
    '6': {
        'a': palindrome('aba'),
        'b': loseprefix('aardvark') == 'rdvark'
    },
    '7': substrings('abc') == ['a', 'ab', 'b', 'abc', 'bc', 'c']
}, sort_keys=True, indent=4))
