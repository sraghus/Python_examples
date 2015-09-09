#!usr/bin/env python

#import modules used here - sys is a very standard one
import sys

def is_even(num):

    '''(int --> bool)
        Return whether num is even.
        >>> is_even(4)
        True
        >>> is_even(77)
        False
    '''
    
    if num % 2 == 0:
        print("True", num)
    else: 
        print("False", num)

        
def is_odd(num):
    if num % 2 == 0:
        print("Even Number", num)
    else:
        print("Odd Number", num)

if __name__ == '__main__':
    is_even(76)
    is_odd(77)
