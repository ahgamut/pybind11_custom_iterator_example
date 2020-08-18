# `pybind11` custom iterator example

This repo contains an example package `primegen` to try out [custom iterator types][pbdoc] noted in
`pybind11`. Implementation is similar to the one provided in [`test_sequences_and_iterators.cpp`][pbgit] in
the `pybind11` Github repo. The package contains:

* `BoundedPrimes` generator and `PrimeIterator` classes in Python, to generate primes until a certain value
* `BoundedPrimes` and `PrimeIterator` classes in C++, wrapped by `pybind11`, to provide the same functionality
	as the Python classes.

## Installation

Requirements same as `pybind11`. Clone the repo and install using `pip`.


## Usage

Run `test_gen.py` and check if the results are identical.

[pbgit]: https://github.com/pybind/pybind11/blob/master/tests/test_sequences_and_iterators.cpp
[pbdoc]: https://pybind11.readthedocs.io/en/stable/advanced/misc.html#binding-sequence-data-types-iterators-the-slicing-protocol-etc
