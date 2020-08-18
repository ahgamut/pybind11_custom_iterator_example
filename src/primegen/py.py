class BoundedPrimes(object):
    def __init__(self, max_val=10):
        super(BoundedPrimes, self).__init__()
        self.max_val = max_val

    def __iter__(self):
        return PrimeIterator(self, return_pairs=False)

    def values(self):
        return PrimeIterator(self, return_pairs=False)

    def items(self):
        return PrimeIterator(self, return_pairs=True)


class PrimeIterator(object):
    def __init__(self, obj, return_pairs):
        super(PrimeIterator, self).__init__()
        self._bound_obj = obj
        self._return_pairs = return_pairs
        self._count = 0
        self._val = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self._val < self._bound_obj.max_val:
            self._val += 1
            if _is_prime(self._val):
                self._count += 1
                if self._return_pairs:
                    return (self._count, self._val)
                else:
                    return self._val
        raise StopIteration()


def _is_prime(p):
    if p <= 1:
        return False
    elif p == 2:
        return True
    elif p > 2 and p % 2 == 0:
        return False
    else:
        i = 3
        while i < 1 + int(p ** 0.5):
            if p % i == 0:
                return False
            i += 2
        return True
