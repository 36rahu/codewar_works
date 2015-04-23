
'''
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer

'''


from math import pow
def square_digits(num):
    return int("".join([str(int(pow(int(i),2))) for i in str(num)]))
