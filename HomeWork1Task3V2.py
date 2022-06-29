def zeros(n):
    enumerator = 0
    while n > 0:
        n = n // 5
        enumerator += n
    return enumerator


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
