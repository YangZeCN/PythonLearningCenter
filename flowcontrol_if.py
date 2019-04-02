'''
Name: flowcontrol_if.py
Author: Yang Ze
Created: 2019.04.02
Last Modified:
Version: V1.0
Description: An example for if...elif...else...
'''

# There is no switch statement in Python. You can use an if..elif..else statement to
# do the same thing (and in some cases, use a dictionary to do it quickly)

number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here
print('Done')
# This last statement is always executed,
# after the if statement is executed.