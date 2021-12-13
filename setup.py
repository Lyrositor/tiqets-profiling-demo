from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["example_6/*.pyx", "example_7/*.pyx"], compiler_directives={"language_level": "3"})
)