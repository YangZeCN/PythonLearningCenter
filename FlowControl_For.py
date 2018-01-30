#Basic example for for loop and range function
for i in range(1, 5):
    print(i)
else:
    print('Example for for loop finished')

#Range() can set the step count, default is 1
'''
for i in range(1, 5, 2):
    print(i)
else:
    print('Example for for loop finished')
'''

#For loop example without using range()
'''
for  i in [1, 4, 5]:
    print(i)
else:
    print('done!')
'''
# Test continue and break function in for loop
for i in range(1, 5):
    if i == 2:
        print('i={}, print(i) doesn\'t execute, and loop continues'.format(i))
        continue
    elif i == 4:
        print('i={}, print(i) doesn\'t execute, and loop breaks'.format(i))
        break
    print(i)
else:
    print('Example for continue and break finished!')  #else can't execute because of the 'break'