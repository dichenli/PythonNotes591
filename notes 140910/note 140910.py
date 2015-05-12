type([1, 2, 3]) #return <type 'list'>
type((1, 2, 3)) #return tuple
#type(1, 2, 3) wrong syntax
[1, 4, (3, 5), "abc", [[4, 5], 6]] # five elements
#enter "_" gives me the list
#_[3] gives me the third element 'abc'
(1, 'a', 4.5, [])
t = _ # now t is the tuple above
t[1] == 'a'
#t[1] = 'b' invalid syntax, tuple can't be changed
divmod(10, 3) == (3, 1) #it's a function, return a tuple.
#in python, a function can only return one value, but it can be a tuple or list,
#so it can return multiple pieces of information
def reverse(t): #badly named, because it only reverse a three-element tuple, so its name is misleading
    return (t[2], t[1], t[0]) #it reverse the order of a tuple or list
reverse((5, 6, 7))
# output will be (7, 6, 5)
reverse([5, 6, 7])
# output will be [7, 6, 5]
reverse([3, 4, 5, 6, 7, 8])
# output will be [5, 4, 3] #works badly as reverse function
reverse('abcdefg')
#output ('c', 'b', 'a')
'abcdefg'[3:7] == 'defg'
p = (3, 5)
x = p[0]
y = p[1]
x == 3
(xx, yy) = p
xx == 3
yy == 5
xxx, yyy = p
xxx == 3
yyy == 5#no need for ()
a, b = 3, 5
a== 3
b == 5 #no need for ()
type((3, 5)) #output tuple
type((1)) #output integer
type((1,)) #output tuple, (1) is int, (1,) change its type to tuple

"""now how to write a test file"""
assert 2 + 2 == 4 #output nothing
assert 2 + 2 == 5 #output wrong message
#Traceback (most recent call last):
#  File "<pyshell#0>", line 1, in <module>
#    assert 2 + 2 == 5
#AssertionError

def third(x):
    assert len(x) >= 3
    return x[2]
third("abcde") #output 'c'
third("ab") #output wrong message
#agile methodologies, an approach for programming
#write test, write code, run test, fail, then rewrite code to run test again. Repeat until test pass.
#The refactor code to make it cleaner. The final code is good enough
#The key is to write test before you write code

#how to write a test file? See arith.py, the file to be tested. Then open note_140910test2

#note_140910test is an earlier version of test file, it import the arith.py as an independent file
