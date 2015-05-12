file1 = open("test.py", 'r')
##for chars in file1:
##    print chars + '\n'
print type(file1)
print file1.readline(), type(file1.readline())
print file1.tell()
print file1.readlines()

file1.close()
def tryinput():
    try: b = input("a number")
    except NameError:
            print "Not recognizable!"
    else:
        if not isinstance(b, int):
            print "Not integer"
            return None
        return b
a = 1
print tryinput()

bb = "avd"
b = [1, 1, 2, 3]
print b.remove(1)
print b
print b.insert(1, 5)
print b
b.sort()
print b
