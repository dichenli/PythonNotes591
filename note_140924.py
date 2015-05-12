{1, 2, 3}#it's a dictionary
set({1, 2, 3})
#now {1, 2, 3} is a set
#in python, a dic and a set both use {}, so to make a set, you need to say set({.......})
#type({}) == <type 'set'>
p = {1, 3, 5, 3, 1, 7}
p == {1, 3, 5, 7} #set don't care about sequence
3 in p == True
q = {1, 3}
q.issubset(p) == True
q.issuperset(p) == False
r = {1, 2, 3, 4, 5}
p.union(r) == {1, 2, 3, 4, 5, 7}
r.union(p) == p.union(r)
r.intersection(p) == {1, 3, 5}
p.difference(r) == {7}
#when you're programming with sets, its elements order may change every time,
#so don't count on the order of elements of a set to be not changed
p.symmetric_difference(r) = {2, 4, 7} #everything that is in one or the other but not in both


#dictionary: like a hash table, a key is assortiated with a value
d = {'one':1, 'two':2, 'three':3}
d['two'] == 2
#d['four'] == Key error, can't find it
'four' in d == False
'one' in d == True
1 in d == False #1 is not a key here
# d['two': 'three'] : error message, you can't point a key to another
d.get('four') == none #d.get() return the value, if no such key, then return None
d.get('one') == 1
d.get('four', 18) == 18 #if not found, return 18 as you put inside
del d['one'] #delete 'one' key
d['four'] = 4 #now 'four'->4 is created
d.pop('four') == 4 #remove 'four'->4 key, also return the value you just took out



