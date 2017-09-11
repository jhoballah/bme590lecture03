import pytest
import sumfxn2

import numpy

import sys
# import iPython
# import pytest
# # import "pytest-cov"
# import "pytest-pep8"

"""

Sums two numbers (positive or negative, decimals allowed)

"""


def testinteger():
    assert(sumfxn2.summation_func(4, 6), 10)


def testfloating():
    assert(sumfxn2.summation_func(-4, 2), 0)


#def testcomplex():
#    assert(sumfxn2.summation_func(3j+1, 3), 4)


def testarguments():
    with pytest.raises(TypeError):
        sumfxn2.summation_func(1)


def teststring():
    with pytest.raises(TypeError):
        sumfxn2.summation_func('a', 'b')

# print("Test 1 result:" + test1integer())
# print("Test 2 result:" + test2floating())
# print("Test 3 result:" + test3string())
