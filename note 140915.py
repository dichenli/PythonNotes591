three = 3 #global
def double(): #local begins
    global three #call global before you use three
    three = 4 
    return 2 * three #local ends
x = double()
print x
print three #now three was changed in double()
def three_times(x):
    def twice(a):  #define a method inside a method
        if a == 1:
            return 2 * a #a local variable in twice().
        else:
            return 2 * x #x is a encircling variable to twice()
    return twice(x) + x

#when a variable is called, the compiler will first find local variable,
#if none, it will look for encircling variable
#if none again, look for global variable
#if none again, look for built in variable (from other files)
#this is called LEGB

def is_even():
    a = '??' #give an initial value
    while a != 'odd' and a != 'even':
#an assertion so that it must be either odd or even before it returns true or false
        a = raw_input("odd or even? ")
    return a == 'even'

def is_even_alt(): #another clever way to do the same thing
    a = raw_input("odd or even? ")
    if a == 'odd' or a == 'even': 
        return a == 'even' 
    return is_even_alt() #recursion! return the function ifself

a = 5
b = a
a = 10
print a, b #b doesn't change as a changes

x = [1, 2, 3]
y = x
x[2] = 4
print x, y #y also changed! x and y are called reference, they are like pointers
#tuple names are also references. But tuple can't be changed once created
#strings are also unchangable. s = 'abc', then s = 'def' will be illegal,
#we can create a new string from the original one though

def mod_first(x):
    x[0] = x[0] + 1
    return 0
w = [1, 2, 3]
mod_first(w)
print w #w was changed in local environment, but w is a reference, so data is still changed
x = 0
def nothing(x):
    x += 1
    return 0
print x #x doesn't change, the x changed only locally






