'''
Name: structures.py
Author: Yang Ze
Created: 2019.04.06
Last Modified:
Version: V1.0
Description:
# An example for data structures, like list, dirtionary, tuple, set
# and addtional introduction to sequence and string
'''

# list [Mutable]
shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist.append('rice')  # add 'rice' to shoplist
del shoplist[0]          # delete the first item of shoplist
shoplist.sort()          # sort the list

# Tuple [Immutable]
zoo = ('python', 'elephant', 'penguin')
new_zoo = 'monkey', 'camel', zoo       # ('monkey', 'camel', ('python', 'elephant', 'penguin'))
'''
# You have to specify it using a comma following the first (and only) item so that 
# Python can differentiate between a tuple and a pair of parentheses surrounding the object in an expression
'''
signleton = (2, )

# Dictionary
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
del ab['Spammer']                # delete Spammer
ab['Guido'] = 'guido@python.org' # add new key-value

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

# Set [Unordered]
bri = set(['brazil', 'russia', 'india'])
'india' in bri     # True
'usa' in bri       # False

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)  # True
bri.remove('russia')
bri & bric # OR bri.intersection(bric)
# result {'brazil', 'india'}


# Sequence & Slicing
# Lists, tuples and strings are examples of sequences
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Character 0 is', name[0])
print('Item 1 to 3 is', shoplist[1:3])  # Slicing
shoplist[::1]   #[start : stop+1 : step]

'''
An assignment statement for lists does not create a copy. You have to use slicing operation to make a copy of the sequence.
'''
newlist = shoplist
del newlist[0]          # newlist & shoplist have the same memory block, so shoplist[0] is deleted too
print(shoplist, newlist)

mylist =  shoplist[:]   # use slicing to create a copy
del mylist[0]
print(mylist, shoplist) # Notice that now the two lists are different


# String [Object]
# This is a string object
name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))    # Brazil_*_Russia_*_India_*_China