'''
Name: basic.py
Author: Yang Ze
Created: 2019.03.31
Last Modified:
Version: V1.0
Description: Basic knowledge of Python
'''

# Name Convention
'''
# Python is case-sensitive, i.e. print != Print
# First character: a letter of the apphabe, or an underscore(_)
# The rest: a letter of the apphabe, underscore(_), or digits(0-9)
# Ensure there is no spaces or tabs before the first character in each line
# Valid name: i, name_2, _Name, Name
# Invalid name: 1_name, this is a space, my-name, >123
'''

# Comments
'''
# Single line comment: #
# Multi line comment: ''' ''', and please note ' == "
# ''' ''' is not the real commnet, instead, it is a string constant, which means it should follow the string syntax rules
'''
# '''\''' will report a worning because of the backslash \
'''\\'''

# Logical & Physical Line
'''
# Python implicitly assumes that each physical line corresponds to a logical line.
# You can combine multiple logical lines on a single physical line by using a semicolon(;). 
# You can break a long logical line into multiple physical lines by using the backslash(\\).
'''
a = 1; b = 2
c = a\
    + b
print(c)

# Constants
'''
# Numbers: 2, 3.23, 3.123E-4
There is no separate long type. The int type can be an integer of any size.

# Strings: 'This is a string'
Strings Are Immutable. There is no separate char data type in Python.
You can specify multi-line strings using triple quotes - (''' ''' or """ """) or \\
'''
string = "This is the first sentence. This is the second sentence."
print(string)
print("This is the first sentence. \
This is the second sentence.")
print('''This is the first sentence.
This is the second sentence.''')

# Escape Sequences & Raw String
''' 
# \t, \n, \\
# 字符串前面添加 r 或者 R，表示该字符串为Raw String，不需要转义
'''
print("Newlines are indicated by \\n.\nThis is the new line")
print(r"Newlines are indicated by \n")

# Indentation
'''
# Use four spaces for indentation.
# Wrong indentation can give rise to errors
'''
i = 5
# Error below! Notice a single space at the start of the line
 print('Value is', i)
print('I repeat, the value is', i)