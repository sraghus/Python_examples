#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    number = float(input("Enter a number: "))
    if number == 0:
        print(int(number), "Zero.")
    elif number % 2 == 0:
        print(int(number), "is Even.")
    elif number % 2 == 1:
        print(int(number), "is Odd.")
    else:
        print(int(number), "is very strange.")


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()



