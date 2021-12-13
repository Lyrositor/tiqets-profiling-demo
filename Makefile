cython:
	python setup.py build_ext --inplace
	find example_6/ -type f -name '*.c' -delete
	find example_7/ -type f -name '*.c' -delete
