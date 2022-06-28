from functools import reduce


def count_find_num(primesL, limit):
    if reduce(lambda x, y: x*y, primesL) > limit:
        return []
    result = list()
    result.append(reduce(lambda x, y: x*y, primesL))
    for a in primesL:
        for b in result:
            b *= a
            while b <= limit and b not in result:
                result.append(b)
                b *= a
    return [len(result), max(result)]

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]


primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

