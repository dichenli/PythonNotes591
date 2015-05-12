#Classes and objects

b = 25 #a global variable

class Stack(object):

    global b #global variable
    b = 30 #global b = 30 is not legal. 
    def __init__(self, x):
        self.my_x = x
        self.stack = []
        #instance variable, instance is synchroname for object

    def print_self(self):
        a = 10
        print self.my_x #my_x is a instance variable, so self. is needed
        print a, "a is a local variable"
        #a is a local variable, so self. is not needed
        print b, "b is a global variable"
        
    def print_twice(self, x):#self is always needed
        print x
        print x
        print self

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def show(self):
        print self.stack

    def push_twice(self, x):
        self.push(x)
        self.push(x)

s = Stack("self x")
print type(s) #it will tell you that s is a Stack class

s.print_twice("print")
#this will call the print twice method
#there is a hidden variable called self

t = Stack("self x")

print s == t
#false

s.print_self()

st = Stack("a stack")
st.show()
st.push(5)
st.push(7)
st.show()
print st.pop()
st.show()
st.push_twice(50)
st.show()

