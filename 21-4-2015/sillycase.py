'''

Create a function that takes a string and returns that string with the first half lowercased and the last half uppercased.

eg: foobar == fooBAR

If it is an odd number then 'round' it up to find which letters to uppercase. See example below.

sillycase("brian")  
//         --^-- midpoint  
//         bri    first half (lower-cased)  
//            AN second half (upper-cased)  


'''


def sillycase(silly):
    if len(silly) % 2 == 0:
        return silly[:len(silly)/2].lower() + silly[len(silly)/2:].upper()
    else:
        return silly[:len(silly)/2+1].lower() + silly[len(silly)/2+1:].upper()
