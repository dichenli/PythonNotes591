b = 8
def bump(b):
    a = 7
    b = 99
    print a, b

bump(6)
print b #b is not changed outside dump

def bump2():
    def foo():
        print x
    x = 99
    foo()
# 99 will be printed, foo is an embedded method


        
