#notes on 140903
#binary: 0b101 == 5
#0x101 == 257; 0x123ABc == 1194684
#0o101 == 65; 0101 == 65
#10 / 3 = 3
#10.0 / 3.0 = 3.3333333333333335 not accurate
                                 #at the last decimal
n = 0
while n != 1:
    n = n + 0.2
    print n
n = 0
while n != 10:
    n = n + 0.2
    print n #won't stop, float number is not accurate
n = 0
#1 + 1.0 = 2.0
#10 / 3 + 1.0 = 4.0
#abs(5) == 5
#abs(-5) == 5
#bin(5) == '0b101'
#oct(5) == '05'
#hex(5) == '0x5'
#ord('a') == 97
#chr(97) == 'a'
v = 'a'
v = chr(ord(v) + 1)
print v #now v == 'b'
