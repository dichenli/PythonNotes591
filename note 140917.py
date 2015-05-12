def foo():
    raise RuntimeError #tell it to make this error intensionally

try: #
    print "\nhere1 foo"
    foo() #call foo

except RuntimeError: #if runtime error, then instead of error message, print what went wrong to output
    print "foo failed!"
print "done" #print done


def notfoo():
    pass #no problem with the method

try:
    print "\nhere2 not foo"
    notfoo() #call notfoo

except RuntimeError:#no error, so no message
    print "foo failed!" 
print "done"

try:
    print "\nhere3 not exist file"
    open('dont_exist.py', 'r')

except Exception:
    print "Can't read file!" 
print "done"

try:
    print "\nhere4 finally"
    raise IOError

except RuntimeError: #won't catch the wrong message
    print "RuntimeError!"

finally: #regardless of what mistakes happened, what's in 'finally' will be done
    print "regardless of what mistakes happened, what's in 'finally' will be done"

print "outside of finally won't be done"
