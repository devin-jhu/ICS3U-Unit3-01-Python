#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The area and perimeter calculator


def main():
    # this function calculates the area and perimeter of a rectangle

    # input
    number_one = int(input("Enter number (integer): "))
    number_two = int(input("Enter number (integer): "))

    # process
    total = number_one + number_two

    # output
    print("")
    print("{0} + {1} = {2}".format(number_one, number_two, total))
    print("Done.")


if __name__ == "__main__":
    main()
