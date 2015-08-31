#!usr/bin/env python

#import modules used here - sys is a very standard one
import sys


def area(base, height):
    return base * height / 2

#if __name__ == '__main__':
#    print('Area :', area(12,23))

#def perimeter(side1, side2, side3):
#	return (side1 + side2 + side3)

#if __name__ == '__main__':
#	print ('Perimeter :', perimeter(12,83,95))


def name():
	input("What is your name? ")

if __name__ == '__main__':
    print name()