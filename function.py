'''
Name: function.py
Author: Yang Ze
Created: 2018.01.30
Last Modified:
Version: V1.0
Description: 
# An example to define function and compare the
# difference between the global and local variable.
'''

global a
a = 10

def global_variable1():
    '''
    Decalre a global variable, and assign a new value to a
    '''
    global a
    a = 2
    print(a)

def global_variable2():
    '''
    Although the variable a was declared at begin, but in this function, it's still a local one
    '''
    a = 10
    print(a)

# print 10
print(a)

# print 2
global_variable1()

# print 2
print(a)

# print 10, the local one in globa_variable2()
global_variable2()

# print 10, the global variable don't be changed
print(a)