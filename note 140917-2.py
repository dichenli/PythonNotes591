abc = 'abc'
abc + abc == 'abcabc'
abc * 10 == 'abcabcabcabcabcabcabcabcabcabc'

n = 0
n += 1
n == 1
n *= 2
n == 2
abc += abc
abc == 'abcabc'

s = 'Dave'.upper()
s == 'DAVE'
s = 'Dave'.lower()
s == 'dave'
a = "computer".find("put")
a == 3 #the third char (count from 0) is the starting point of 'put' in the string
c = "Computer Science"
c.endswith("e") == True
c.endswith("nce") == True
c.endswith("E") == False
c.startswith("Com") == True
cstar = c.replace('e', '**')
cstar == "Comput**r Sci**nc**"
c.isalnum() == False #
s = '   Computer\t Science   \t'
print s, 'endofstring'
ss = s.strip() #remove all white spaces in the beginning and the end of a string
print ss, 'endofstring'
rs = r'\n\t' #r means not change \n, \t etc to change line, tab, etc.
print rs
rs2 = '\\n\\t' #work similarly
