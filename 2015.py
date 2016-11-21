import json


def area(x1, x2, x3, y3):
    return abs((x2 - x1) * y3 / 2)


def inner(x1, x2, x3, y3):
    return (((x2 - x1) / 2, (x3 - x1) / 2, (x2 - x3) / 2), (0, y3 / 2, y3 / 2))


def flip(x1, x2, x3, y3):
    return (x1, x2, x3, -y3)


def inside(x1, y1, r1, x2, y2, r2):
    return r2 > r1 + ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)


def one(b1, b2, b3):
    return 1 is len([b for b in [b1, b2, b3] if not b])


def fits(b1, b2, n):
    return n is len([b for b in [b1, b2] if b])


def countWords(string, caseSensitive=False):
    string = string if caseSensitive else string.lower()
    words = dict()
    for word in string.split():
        words[word] = 1 + words.get(word, 0)
    return [i for k, v in words.items() for i in [k, v]]


def nameDomain(email):
    return email.split('@')[0].split('.') + [email.split('@')[1]]


def accum(xlist):
    acc = []
    sum = 0
    for i in xlist:
        sum += i
        acc.append(sum)
    return acc


def decum(ylist):
    dec = []
    last = 0
    for i in ylist:
        dec.append(i - last)
        last = i
    return dec


def mix(listA, listB):
    return [[a, b] for a, b in zip(listA, listB)]


def unmix(listC):
    return ([x[0] for x in listC], [x[1] for x in listC])


def marksDistribution(marks):
    def count(marks, mini, maxi):
        return len([n for n, mark in marks.items() if mini <= mark <= maxi])
    return {
        '0-20': count(marks, 0, 20),
        '21-40': count(marks, 21, 40),
        '41-60': count(marks, 41, 60),
        '61-80': count(marks, 61, 80),
        '81-100': count(marks, 81, 100),
    }


def quick_sort(lst):
    return lst if len(lst) < 2 else \
        quick_sort([i for i in lst if i < lst[0]]) + \
        [i for i in lst if i == lst[0]] + \
        quick_sort([i for i in lst if i > lst[0]])


print(json.dumps({
    '1': {
        'a': area(0, 10, 0, 10) == 50,
        'b': inner(0, 10, 0, 10) == ((5, 0, 5), (0, 5, 5)),
        'c': flip(0, 10, 0, 10) == (0, 10, 0, -10),
    },
    '2': {
        'a': inside(2, 2, 4, 3, 3, 5) is False,
        'b': one(True, False, True),
        'c': fits(True, False, 1) is True
    },
    '3': {
        'a': countWords('best of the best') == ['of', 1, 'the', 1, 'best', 2],
        'b': nameDomain('r.w@uwa.edu') == ['r', 'w', 'uwa.edu']
    },
    '4': {
        'a': accum([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15],
        'b': decum([1, 3, 6, 10, 15]) == [1, 2, 3, 4, 5]
    },
    '5': {
        'a': mix(['a', 'b', 'c'], [1, 2, 3]) == [['a', 1], ['b', 2], ['c', 3]],
        'b': unmix([['a', 1], ['b', 2]]) == (['a', 'b'], [1, 2])
    },
    '6': marksDistribution({
        # 'mark': 24,
        'lucy': 58,
        'mark': 43,
        'andy': 84
    }) == {
        '0-20': 0,
        '21-40': 0,
        '41-60': 2,
        '61-80': 0,
        '81-100': 1
    },
    '7': quick_sort([8, 1, 4, 3, 2]) == [1, 2, 3, 4, 8]
}, sort_keys=True, indent=4))
