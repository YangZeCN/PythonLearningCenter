'''
Name: module_name.py
Author: Yang Ze
Created: 2019.04.05
Last Modified:
Version: V1.0
Description:
# An example for __main__
'''

# Every Python module has its __name__ defined. If this is '__main__' , that implies that the
# module is being run standalone by the user and we can take appropriate actions.

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')