'''

Format a string of names like 'Bart, Lisa & Maggie'.

Description:

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''


Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

'''

def namelist(names):
    out = [i['name'] for i in names]
    if len(out) == 0:
        return ''
    elif len(out) == 1:
        return out[0]
    elif len(out) == 2:
        return " & ".join(out)
    else:
        return ", ".join(out[:-1])+" & "+out[-1]
