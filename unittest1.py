import pytest


def test (num1, num2):

def testinteger ():
   assert (summation_func(4,6),10)

def testfloating ():
   assert (summation_func(-4,2),0)

def testcomplex ():
   assert (summation_func(3j+1, 8),9)

def testargument ():
   with pytest.raises(NotEnoughArguments):
	   summation_func(1)

print("Integer Test Result:" + testinteger())
print("Floating Test Result:" + testfloating())
print("Complex Test Result:" + testcomplex())
print("String Test Result:" + teststring())
print("Argument Test Result:" + testargument())





