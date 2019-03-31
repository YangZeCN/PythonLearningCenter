'''
Name: basic_format.py
Author: Yang Ze
Created: 2019.03.31
Last Modified:
Version: V1.0
Description: Introduce the usage of format()
'''

# Basic example of 'String'.format()
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# The number in {} can be omitted
print('{} was {} years old when he wrote this book'.format(name, age)) 

'''
1. {}+format可以定义输出的格式，{name:_^11}这种方式也行
2. {}后面如果不加format，则认为是普通字符串
3. {}和format中参数个数必须对应，否则报错；但顺序不需对应，只需变量名一致
eg: print('{name} wrote {book}'.format(book='Python', name='zy'))
4. format中不同的参数类型会自动转换成字符串
'''
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print('{name} wrote {book}'.format(book='Python', name='zy'))