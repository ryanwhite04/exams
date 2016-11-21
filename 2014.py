import json


def perimeter(x1, y1, x2, y2):
    return 2 * (abs(x2 - x1) + abs(y2 - y1))


def crossesAxis(x1, y1, x2, y2):
    return abs(x1) < abs(x2 - x1) > abs(x2) or \
        abs(y1) < abs(y2 - y1) > abs(y2)


def square(x1, y1, x2, y2):
    length = ((x2 - x1) * (y2 - y1))**(0.5)
    x = int(length - abs(x2 - x1)) / 2
    x = -x if x1 < x2 else x
    y = int(length - abs(y2 - y1)) / 2
    y = -y if y1 < y2 else y
    return (x1 + x, y1 + y, x2 - x, y2 - y)


def valid(x, y, z):
    a = len([i for i in [x, y, z] if i >= 0])
    b = len([i for i in [x, y, z] if i < 0]) < 2
    return a and b


def test_valid():
    return all([
        not valid(-1, -1, -1),
        not valid(-1, -1,  1),
        not valid(-1,  1, -1),
        valid(-1,  1,  1),
        not valid(1,  -1, -1),
        valid(1,  -1,  1),
        valid(1,   1, -1),
        valid(1,   1,  1),
    ])


def between(x, y, z):
    return [i for i in range(x, y + 1) if not i % z]


def smooth(xs):
    return [(a + b)/2.0 for a, b in zip(xs[:-1], xs[1:])]


def ascending(xs):
    asc = [xs[0]]
    for i in xs:
        if i > asc[-1]:
            asc.append(i)
    return asc


def positive(xs):
    pos = []
    sum = 0
    for i in xs:
        sum = sum + i
        if sum > 0:
            pos.append(i)
        else:
            return pos


def maximal(xs):
    sort = sorted(xs, key=lambda k: k[1])
    maxi = [sort[0]]
    for i in sort:
        if i[0] > maxi[-1][1]:
            maxi.append(i)
    return maxi


def balanced(s):
    def toNumber(bracket):
        if bracket is '(':
            return 1
        elif bracket is ')':
            return -1
        else:
            return 0
    numbers = [toNumber(i) for i in s]
    sum = 0
    for i in numbers:
        sum = i + sum
        if sum < 0:
            return False
    return not sum


def partition(s):
    d = dict()
    for word in s.split():
        d[len(word)] = d.get(len(word), []) + [word]
    return d


print(json.dumps({
    '1': {
        'a': perimeter(2, -2, 10, 10) is 40,
        'b': crossesAxis(2, -2, 10, 10),
        'c': square(2, -2, 18, 2) == (6, -4, 14, 4)
    },
    '2': {
        'a': valid(-1,  1,  1),
        'b': test_valid()
    },
    '3': {
        'a': between(6, 20, 4) == [8, 12, 16, 20],
        'b': smooth([3, 5, 2, 6, 7, 3]) == [4.0, 3.5, 4.0, 6.5, 5.0]
    },
    '4': {
        'a': ascending([2, 1, 5, 3, 5, 1, 6, 6, 7, 0]) == [2, 5, 6, 7],
        'b': positive([3, 2, -4, 2, -7, 5, 21]) == [3, 2, -4, 2]
    },
    '5': maximal([(2, 4), (1, 7), (5, 9), (9, 11)]) == [(2, 4), (5, 9)],
    '6': balanced('(())()') and not balanced(')()'),
    '7': partition('Wales will win the World Cup twice') == {
        3: ['win', 'the', 'Cup'],
        4: ['will'],
        5: ['Wales', 'World', 'twice']
    }
}, sort_keys=True, indent=4))
