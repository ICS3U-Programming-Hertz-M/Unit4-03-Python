#!/usr/bin/env python3

# Created by: Hertz
# Created on: Apr, 23, 2022
# This program asks the user to enter a number. It then displays the
# power of two from 0 to the user number.


def main():
    # initialize the loop counter and power_of_two
    counter = 0
    power_of_two = 0

    # get the user number as a string
    user_number_string = input("Enter a positive number:")
    print("")

    try:
        # converts user input to integer and
        # calculate the factorial of the user using loops.
        user_number_int = int(user_number_string)
        if user_number_int >= 0:
            for counter in range(user_number_int + 1):
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))
                counter = counter + 1

        else:
            print("Please enter a positive number(1,2,3..")
    except Exception:
        print(" Invalid number.")


if __name__ == "__main__":
    main()
