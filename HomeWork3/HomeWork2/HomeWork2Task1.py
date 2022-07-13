from custom_range import Range3


class CyclicIterator:

    def __init__(self, obj):
        self.obj = obj
        self.iterator = iter(self.obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.obj)
            return next(self.iterator)


if __name__ == '__main__':
    for i in CyclicIterator(Range3(5)):
        print(i)
