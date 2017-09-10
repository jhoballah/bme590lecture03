import numpy
import sys
# import ipython
# import pytest
# import pytest-cov
# import pytest-pep8

"""

Sums two numbers (positive or negative, decimals allowed)

"""
class NotEnoughArguments(TypeError):
    """ Raised when the number of arguments is invalid"""

class NotNumberError(ValueError):
    """ Raised when the input is not a number """
    pass


def summation_func(num1, num2):
    try:
        sys.argv = 2
        pass

    except NotEnoughArguments:
        print("You need to input two numbers for summation!")
        raise NotNumberError

    try:
        num1 = complex(num1)
        num1 = num1.real
    except ValueError:
        print("Your first input is not a number, please input a number.")
        raise NotNumberError

    try:
        num2 = complex(num2)
        num2 = num2.real

    except ValueError:
        print("Your second input is not a number, please input a number.")
        raise NotNumberError

    sum_num = num1 + num2

    if sum_num >= 0:
        print('Your sum is %.2f' % sum_num)
        return sum_num
    else:
        sum_num = 0
        print("Your sum is %.2f" % sum_num)
        return sum_num
