'''
Name: function_argument.py
Author: Yang Ze
Created: 2018.02.01
Last Modified:
Version: V1.0
Description:
# An example for default argument, keyword argument, VarArgs parameters, etc.
'''

def default_argument(a, b, c=2, d='m'):
    '''The last two parameters b and c have defualt value;
    Only those parameters which are at the end of the parameter list can be given default argument values;
    def defualt_argument(a=1, b, c='m') is invalid'''
    print(a, b, c, d)


def var_argument(a='Jack', *name, **age):
    '''Pass variable number of argument by using star
    More detailed information, pls refer to data structure'''
    print(a)
    print(name)
    print(age)
    # dict_items
    print(age.items())

    for student_name in name:
        print(student_name)
    # not for...in age, property/method 'item' is followed by 'age'
    for student_name, student_age in age.items():
        print(student_name, student_age)

'''Call the function in regular way and defualt argument way'''
# Output: lm a 1 5
default_argument('lm', 'a', 1, 5)
# output: 1 q 2 m
default_argument(1, 'q')

'''By using keyword, we needn't to send argument in order
but we must make sure that the arguments without keyword are at the front of list by order
defualt_argument(c=1, 'q', a=5) is invalid'''
# output: 5 q 1 3
default_argument(c=1, b='q', a=5, d=3)
# output: l p 3 m
default_argument('l', c=3, b='p')

# var_argument('Green', 'James', 'Li lei',  Jack=10, 'Jack', Jerry=2, Tom=21) is invalid
var_argument('Green', 'James', 'Li lei', 'Jack', Jack=10, Jerry=2, Tom=21)
'''
Green
('James', 'Li lei', 'Jack')
{'Jack': 10, 'Jerry': 2, 'Tom': 21}
dict_items([('Jack', 10), ('Jerry', 2), ('Tom', 21)])
James
Li lei
Jack
Jack 10
Jerry 2
Tom 21
'''

# print the docstring of function defualt_argument
print(default_argument.__doc__)