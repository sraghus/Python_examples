#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    # a = 0
    # while a < 10:
    #     a = a + 1
    #     if a > 5:
    #         print(a, ">", 5)
    #     elif a <= 3:
    #         print(a, "<=", 3)
    #     else:
    #         print("Neither test was true")

    fahr_temp = float(input("Fahrenheit temperature: "))
    print("Celsius temperature: ", (fahr_temp - 32.0) * 5.0 / 9.0)

    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()




