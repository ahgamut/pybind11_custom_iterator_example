#include <cmath>
#include <utility>
#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace pgen
{
    struct BoundedPrimes
    {
        long max_val;
        BoundedPrimes(long m_val = 10) : max_val(m_val){};
    };

    bool isPrime(long p)
    {
        if (p <= 1)
            return false;
        else if (p == 2)
            return true;
        else if (p % 2 == 0)
            return false;
        else
        {
            long ub = static_cast<long>(std::sqrt(p)) + 1;
            for (long i = 3; i < ub; i++)
                if (p % i == 0) return false;
            return true;
        }
    }

    class PrimeIterator
    {
       public:
        PrimeIterator(const BoundedPrimes& obj, py::object ref) : obj(obj), ref(ref)
        {
            count = 0;
            val = 1;
        };
        long next_prime()
        {
            while (val < obj.max_val)
            {
                val++;
                if (isPrime(val))
                {
                    count++;
                    return val;
                }
            }
            throw py::stop_iteration();
        };

       private:
        const BoundedPrimes& obj;
        py::object ref;
        long val;
        long count;
    };
    class PrimePairIterator
    {
       public:
        PrimePairIterator(const BoundedPrimes& obj, py::object ref) : obj(obj), ref(ref)
        {
            count = 0;
            val = 1;
        };
        std::pair<long, long> next_prime()
        {
            while (val < obj.max_val)
            {
                val++;
                if (isPrime(val))
                {
                    count++;
                    return std::make_pair(count, val);
                }
            }
            throw py::stop_iteration();
        };

       private:
        const BoundedPrimes& obj;
        py::object ref;
        long val;
        long count;
    };

}  // namespace pgen

PYBIND11_MODULE(cpp, m)
{
    using namespace pybind11;
    class_<pgen::BoundedPrimes>(m, "BoundedPrimes")
        .def(py::init<long>())
        .def_readonly("max_val", &pgen::BoundedPrimes::max_val)
        .def("__iter__",
             [](py::object s) {
                 return pgen::PrimeIterator(s.cast<const pgen::BoundedPrimes&>(), s);
             })
        .def("values",
             [](py::object s) {
                 return pgen::PrimeIterator(s.cast<const pgen::BoundedPrimes&>(), s);
             })
        .def("items", [](py::object s) {
            return pgen::PrimePairIterator(s.cast<const pgen::BoundedPrimes&>(), s);
        });
    class_<pgen::PrimeIterator>(m, "PrimeIterator")
        .def("__iter__", [](pgen::PrimeIterator& it) { return it; })
        .def("__next__", &pgen::PrimeIterator::next_prime);
    class_<pgen::PrimePairIterator>(m, "PrimePairIterator")
        .def("__iter__", [](pgen::PrimePairIterator& it) { return it; })
        .def("__next__", &pgen::PrimePairIterator::next_prime);
}
