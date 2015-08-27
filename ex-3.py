#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    number = 8
    guess = -1

    print("Guess the number!")
    while guess != number:
        guess = int(input("Is it..."))

        if guess == number:
            print("Hooray! you guessed it right!")
        elif guess < number:
            print("It's bigger")
        elif guess > number:
            print("It is not so big.")


# Numbers to add to the Sum 

#def test():
#    a = 1
#    s = 0
#    while a != 0:
#        print("Current Sum: ", s)
#        a = float(input("Number? "))
#        s = s + a
#        print('Total Sum = ', s)


    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

#def test():
#password = str()
#while password != "sreerama"
#    password = input("Password: ")
#print("Welcome in")

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()



