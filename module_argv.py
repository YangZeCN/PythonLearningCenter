'''
Name: module_argv.py
Author: Yang Ze
Created: 2018.02.05
Last Modified:
Version: V1.0
Description:
# An example for importing module and reading command line argument.
'''

# import sys modudle
import sys

# print sys.argv, it's a list of the command line argument
print(sys.argv)

for i in sys.argv:
    print(i)

'''If we use 'python xx/module_argv.py -a -l' to call this file,
the result printed will be
    ['xx\module_argv.py', '-a', '-l']
    xx\module_argv.py
    -a
    -l
which means we can use sys.argv to get the command line argument'''
