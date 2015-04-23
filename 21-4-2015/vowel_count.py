'''

Return the number(count) of vowels in the given string. We will consider a, e, i, o, and u as vowels for this kata.


'''


def getCount(inputStr):
    return len(inputStr)-len(inputStr.translate(None,'aeiou'))
