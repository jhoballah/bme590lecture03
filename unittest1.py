import pytest

def Jawad_placeholder (input1, input2):



def test1integer ():
	assert (Jawad_placeholder(4,6),10)

def test2floating ():
	assert (Jawad_placeholder(-4,2),0)

def test3string ():
	assert (Jawad_placeholder('word',3),'NaN')



print("Test 1 result:" + test1integer())
print("Test 2 result:" + test2floating())
print("Test 3 result:" + test3string())


