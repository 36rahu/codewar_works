'''

Description:
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters that occur more than once in the given string. The given string can be assumed to contain only uppercase and lowercase alphabets.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'

'''

from operator import add
def duplicate_count(text):
    a = "abcdefghijklmnopqrstuvwxyz"
    out1 = [text.count(i) for i in a.lower()]
    out2 = [text.count(i) for i in a.upper()]
    out = map(add,out1,out2)
    out = filter(lambda a: a !=1 and a !=0, out)
    return len(out)
