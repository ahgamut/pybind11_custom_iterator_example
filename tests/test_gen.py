import primegen
import pytest


def test_py():
    b = primegen.BoundedPrimesPy(15)
    assert list(x for x in b) == [2, 3, 5, 7, 11, 13]
    assert list(x for x in b.values()) == [2, 3, 5, 7, 11, 13]
    assert list(x[1] for x in b.items()) == [2, 3, 5, 7, 11, 13]


def test_cpp():
    b = primegen.BoundedPrimesCpp(15)
    it = b.values()
    next(it)
    next(it)
    next(it)
    next(it)
    next(it)
    next(it)
    with pytest.raises(StopIteration):
        next(it)
    assert list(x for x in b) == [2, 3, 5, 7, 11, 13]
    assert list(x for x in b.values()) == [2, 3, 5, 7, 11, 13]
    assert list(x[1] for x in b.items()) == [2, 3, 5, 7, 11, 13]


def test_same():
    b1 = primegen.BoundedPrimesPy(81)
    b2 = primegen.BoundedPrimesCpp(81)
    assert list(x for x in b1) == list(x for x in b2)
    assert list(x for x in b1.values()) == list(x for x in b2.values())
    assert list(x for x in b1.items()) == list(x for x in b2.items())
