from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from distutils.command.build import build as _build
import sys
import os
import platform


VERSION = "0.1.0"


class get_pybind_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked. """

    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11

        return pybind11.get_include(self.user)


ext_modules = [
    Extension(
        name="primegen.cpp",
        sources=["src/primegen/cpp.cpp"],
        include_dirs=[str(get_pybind_include(True)), str(get_pybind_include(False)),],
        language="c++",
    )
]


class BuildExt(_build_ext):
    """A custom build extension for adding compiler-specific options."""

    c_opts = {
        "msvc": ["/EHsc", "/std:c++14"],
        "unix": ["-Wall", "-Wpedantic", "-Wno-unused-result", "-std=c++14"],
    }

    if platform.system() == "Windows":
        os.environ["CC"] = "msvc"
        os.environ["CXX"] = "msvc"

    if sys.platform == "darwin":
        c_opts["unix"] += ["-stdlib=libc++", "-mmacosx-version-min=10.7"]

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct)
        if ct == "unix":
            opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
            opts.append("-fvisibility=hidden")
        elif ct == "msvc":
            opts.append('-DVERSION_INFO=\\"%s\\"' % self.distribution.get_version())
        else:
            raise ValueError("Compiler unknown")
            opts = self.c_opts.get("unix")
        for ext in self.extensions:
            ext.extra_compile_args = opts
            if "mingw" in ct:
                ext.extra_link_args = [
                    "-Wl,-Bstatic,--whole-archive",
                    "-lwinpthread",
                    "-Wl,--no-whole-archive",
                    "-static-libgcc",
                    "-static-libstdc++",
                ]
        _build_ext.build_extensions(self)


with open("./README.md") as f:
    long_description = f.read()

setup_info = dict(
    name="primegen",
    version=VERSION,
    author="Gautham Venkatasubramanian",
    author_email="ahgamut@gmail.com",
    url="https://github.com/ahgamut/pybind11_custom_iterator_example",
    description="Example package using pybind11 custom iterators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license="not set",
    packages=find_packages("src"),
    package_dir={"": "src"},
    ext_modules=ext_modules,
    install_requires=["pybind11>=2.2"],
    setup_requires=["pybind11>=2.2"],
    cmdclass={"build_ext": BuildExt},
)

setup(**setup_info)
