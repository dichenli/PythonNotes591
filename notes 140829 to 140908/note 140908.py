bin(13) == '0b1101'
0b1101 == 13 #0b1101 is a number 13, '0b1101' is a string
0100 == 64 #octa

print oct(64) == '0100'
#0468 : invalid syntax, 8 shown

0x19abcdef == 430689775
hex(430689775) == 0x19abcdef

#'123' + 1 : invalid syntax
int('123') + 1 == 124

#int('0x100') : invalid
int(0x100) == 256

ord('a') == 97 #ASCII code
ord('A') == 65
#'a' + 1 == invalid
ord('a') + 1 == 98 #ord change char to number.
chr(ord('a') + 1) == 'b' #chr function change number to character
num = "a" #"" or '' doesn't matter
chr(ord(num) + 1) == 'b'
10 / 3 == 3 #in python 3 version, 10 / 3 == 3.333333333
10 % 3 == 1
10 // 3 == 3 #in python 3, // is to do traditional divisions, so 10 // 3 == 3, 10 / 3 == 3.33333.
#in python 2 we use, either are the same
divmod (10, 3) == (3, 1) # (dividend, reminant)

import math
math.pi == 3.141592653589793
int(5.9999) == 5
round (5.99) == 6.0

eval('2 + 3 * 4') == 14 #??

t = ('a', 77, 5.3, True) #a tuple
t[0] == 'a'
t[3] == True
t[-1] == t[3] # it's circulated
t[-2] == t[2]
t[-3] == t[1]
t[-4] == t[0]
#t[1] = 1009 : invalid. Once the contents of a tuple is created, it can't be changed.
t + (1, 2, 3) == ('a', 77, 5.3, True, 1, 2, 3) #but t doesn't change here

li = ['a', 77, 5.3, True] # it's a list
li[-1] == True  # it's circulated
li[1] = 1009 # now li == ['a', 1009, 5.3, True]
#li press enter, show li contents

range(0, 11) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = range(0,11)
nums[5] == 5
nums[5:8] == [5, 6, 7]
nums[5:] == [5, 6, 7, 8, 9, 10]
nums[:5] == [0, 1, 2, 3, 4] #not including 5!
[1, 2, 3] + [7] == [1, 2, 3, 7]
nums[:8] + nums [8:] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums[8:] + nums [:8] == [8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7]
# nums[-5:-7] invalid
nums[-5:-7] == []
nums[-7:-5] == [4, 5]

