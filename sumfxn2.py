# import numpy
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
    pass

class NotNumberError(ValueError):
    """ Raised when the input is not a number """
    pass


def summation_func(num1, num2):
    if (len(sys.argv) != 2):
        raise TypeError('You need to input two numbers for summation!')

    if (type(num1)== type(str) or type(num2)==type(str)):
        raise TypeError('You need to input two numbers for summation!')

#    if (complex(num1) or complex(num2)):
#        raise NotNumberError('Your first input is not a number, please input a number.')

    sum_num = num1 + num2

    if sum_num >= 0:
        print('Your sum is %.2f' % sum_num)
        return sum_num
    else:
        sum_num = 0
        print("Your sum is %.2f" % sum_num)
        return sum_num
