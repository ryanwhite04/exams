import json


def area(x1, y1, x2, y2):
    return abs((x2 - x1) * (y2 - y1))


def half(x1, y1, x2, y2):
    return (
        1 + x1 * 3/4 + x2 * 1/4,
        1 + y1 * 3/4 + x2 * 1/4,
        1 + x2 * 3/4 + x1 * 1/4,
        1 + y2 * 3/4 + y1 * 1/4
        )


def flip(x1, y1, x2, y2):
    return (
        min(x1, x2),
        min(y1, y2),
        min(x1, x2) + abs(y2 - y1),
        min(y1, y2) + abs(x2 - x1)
    )


def one(x, y, z):
    return len([i for i in [x, y, z] if i]) == 1


def test_one():
    return all([
        not one(0, 0, 0),
        one(0, 0, 1),
        one(0, 1, 0),
        not one(0, 1, 1),
        one(1, 0, 0),
        not one(1, 0, 1),
        not one(1, 1, 0),
        not one(1, 1, 1)
    ])


def alternating(xs):
    last = not xs[0]
    for i in xs:
        if last == i:
            return False
        last = i
    return True


def triangle(xs):
    lol = []
    count = 0
    while count < len(xs):
        count += 1
        lol.append(xs[0:count])
        xs = xs[count:]
    return lol


def fives(n):
    return [i for i in range(n + 1) if str(i).count('5')]


def diagonals(n):
    return [[i + j for j in range(n)] for i in range(n-1, -1, -1)]


def simple(xs):
    sim = [0]
    last = True
    for i in xs:
        if i == last:
            sim[-1] += 1
        else:
            sim.append(1)
        last = i
    return sim


def third(xs):
    length = len(xs)
    return xs[int(length * 1/3):int(length * 2/3)]


def middle(x, s):
    return s[s.find(x) + 1:s.rfind(x)]


def rabbits(n, m=12, i=0):
    return rabbits(n - 1, m + i, int(m/3)) if n else (m, i)


print(json.dumps({
    '1': {
        'a': area(2, -2, 10, 10) is 96,
        'b': half(2, -2, 10, 10) == (4, 1, 8, 7),
        'c': flip(2, -2, 10, 10) == (2, -2, 14, 6)
    },
    '2': {
        'a': one(0, 0, 1),
        'b': test_one()
    },
    '3': {
        'a': alternating([False, True]) and not alternating([True, True]),
        'b': triangle([9, 7, 2, 4, 6, 1, 0, 5]) == [[9], [7, 2], [4, 6, 1]]
    },
    '4': {
        'a': fives(25) == [5, 15, 25],
        'b': diagonals(3) == [[2, 3, 4], [1, 2, 3], [0, 1, 2]]
    },
    '5': simple([False, True, True, False, False, False]) == [0, 1, 2, 3],
    '6': {
        'a': third('Python') == 'th',
        'b': middle('n', 'Lyndon money') == 'don mo'
    },
    '7': rabbits(2) == (16, 4)
}, sort_keys=True, indent=4))
