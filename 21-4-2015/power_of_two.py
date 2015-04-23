'''

Description:

Write a function that determines if given number is a power of two. A power of two means a number of the form 2^n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent. I.e. 1024 is a power of two: it 2^10.

power_of_two(4096) # true

power_of_two(333) # false

Pay attention: hidden tests are using extremmely big numbers

'''

from math import log

def power_of_two(x):
    if str(log(x)/log(2)).split(".")[1] == '0':
        return True
    else:
        return False
