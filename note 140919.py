a = input() #read in an input, then call eval() to decide what input it is and return
b = raw_input() #return a string
c = eval('1')
#eval evaluate what's inside the '' to judge what legal Python expression it is
print a, b, c


#open file
file = open('test.py', 'r')
#file = open('a name', a mode)
#modes are 'r' 'w' or 'a' mode decides what you open the file for
#read it, write on it, or attach it
#name is a string of directory, such as 'C:/...'
#if the file is in the same directory as your program is, you can use file name directly
a = file.read()
b = file.readline() #it returns a string with \n in the end
c = file.readlines()
print a, b, c
#file.readlines()

#file writing

file = open('test.py', 'w')
file.write('print "a"')
file.close

import os
dir = os.getcwd()#get current working directory
dir = os.chdir(path)
os.rename(oldname, newname)
