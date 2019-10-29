#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This lets the user guess a number

import random


def main():
    #  counts how many tries taken
    tries = 1

    while True:
        # random number
        number = random.randint(0, 9)

        # input
        guess_as_string = input("Guess my number between 0 and 9: ")

        # process & output
        try:
            # converts number as string to integer
            guess_as_number = int(guess_as_string)

            # process
            if guess_as_number == number:
                # output
                print()
                print("Correct! My number was", number)
                print("It took you", tries, "tries to guess my number")

            # process
            elif guess_as_number != number:
                # output
                tries += 1
                print()
                print("Sorry, thats not it")
                print("Keep trying")
                print()
                continue

        except ValueError:
            print()
            print("This is not a integer")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
