'''
Name: basic.py
Author: Yang Ze
Created: 2019.03.31
Last Modified:
Version: V1.0
Description:
# Examples for operators
'''

# plus +
''' 3 + 5 = 8, 'a' + 'b' = 'ab' '''
print(3 + 5)
print('a' + 'b')

# minus -
''' same as normal '-' '''
# unsupported operand type(s) for -: 'str' and 'str'
# print('ab'-'a') will reprot error

# multiply *
''' 3 * 5 = 15, 'a' * 3 = 'aaa' '''
print('a' * 3)

# power **
''' 3 ** 5 = 243 = 3 * 3 * 3 * 3 * 3 '''
print(3 ** 5)

# divide /
''' 9 / 3 = 3 '''
print(9 / 3)

# divide and floor //
''' Divide x by y and round the answer down to the nearest integer value '''
print(13 // 3)    # 4
print(13 // 2.51) # 5.0

# modulo %
''' Returns the remainder of the division '''
print(13 % 3)     # 1
print(-13 % 3)    # 2

# shift << >>
print(11 >> 1)    # 5, 1011 >> 101

# bit wise
# &, |, ^, ~
print(~5)         # -6, ~x = -(x+1), ~0101 = 1010 = -6

# logic
# <, >, <=, >=, ==, !=
''' Return True/False '''
print(3 < 5 < 7)     # True
print(3 < 5 > 7)     # False
# not, and, or
'''
Number：0 = False，others = True
String：Null = False，others = True
not return True/False
short-circuit evaluation
# a and b, if a = True, return b; else return False
# a or b, if a = True, return a; else returen b
'''
a = 1
b = 'Test'
c =  False
print(a and b)      # 'Test'
print(a or b)       # 1
print(c and b)      # False
print(c or b)       # 'Test'
