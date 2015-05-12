print "some notes about programming ABC's"
age = raw_input("what is your age (string)?") #type in a string and enter
print age
age1 = input("What is your age (int)?") #type in a number
print age 
print age1, 2 + 2, "age"  #use spaces after operators, commas, no spaces on either sides of parathesis
if age1==1 or age1>=10: #use :
    print "1 or >=10"
elif age1==2:
    print "age =", 2
else:
    print "else"
print "tab:\ttabends" # a tab in string: \t
#If you use someone's line, quote whose or where from

print "Now about random number"
import random #import a function or what??
n = 1
while n != 2:
    n = random.randint(1, 10) # asign a random integar to n between 1 and 10 (1,2,3,4...)
    print n

print "Now about for"
for n in [1, 2, 4]:
    print n
for n in range(1, 4):
    print -n

print "Now about list"
courses = ['CIT 591', 'CIT 592', 'CIT 593'] #list is a sequence in brackets
print courses[0], courses[1], courses[2], len(courses) #courses is now a list name. "len" function returns the size of the list
range1 = range(2, 5) #range is a list, now [2, 3, 4], not 5
for k in range1:
    print k
range2 = range(2, 5, 2) #the 3rd number is the step
for k in range2:
    print k

print "Now about function"
def sum(numbers):
    """This function calculates the sum""" # """something something""" a convention, to tell what this function does
    total = 0
    for number in numbers:
        total = total + number
    return total
n = sum(range1)
m = sum (range2)
print n, m
