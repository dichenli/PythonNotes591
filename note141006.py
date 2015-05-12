def uniq(str):
    """remove all duplicates in a string"""
    if len(str) <= 1:
        return str
    else:
        return str[0] + uniq(str.replace(str[0], ''))
#str.replace do replace all the same char1 to char2
#it works by recursion.

def translate(message, dictionary):
    return ''.join(map(lambda ch: dictionary.get(ch, ch), message))


#map(fun, list) method gives a function to map every elem in the list to a new elem.
#function can be defined like below:
#map(lambda ch: dictionary.get(ch, ch), list)

#dictionary is a hash, dictionary.get(ch) will find the value given a key ch. The second variable here
#dictionary.get(ch, ch) means if no value is found, return the second variable
#lambda means we will define a function here
#lambda a : b means given a, it returns b
#''.join means join a string after ''

x = [1, 2]
y = [3, 4]
z = zip(x, y) #make a list of tuples.
print z #=> [(1, 3), (2, 4)]
x2, y2 = zip(*z) #unzip
print x2, y2
x2 == x, y2 == y

