import redis


def memory(foo):
    cache = redis.Redis(host='localhost', port=6379, db=0)
    assert(cache.ping() == 1)

    def wrapper(number):
        if not cache.exists(number):
            cache.set(number, foo(number))
        return int(cache.get(number))
    return wrapper


@memory
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    assert (multiplier(15) == 30)
    assert (multiplier(0) == 0)
    assert (multiplier(-32) == -64)
    assert (multiplier(-32) == -64)
    assert (multiplier(15) == 30)
    assert (multiplier(0) == 0)
    print(multiplier(7))
