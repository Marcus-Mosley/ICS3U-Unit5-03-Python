#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on November 2020
# This program converts a student's mark into a percentage


def percent_convert(mark):
    # This function converts a student's mark into a percentage

    if "4+" in mark:
        percent = 98
    elif "4" in mark:
        percent = 91
    elif "4-" in mark:
        percent = 83
    elif "3+" in mark:
        percent = 78
    elif "3" in mark:
        percent = 75
    elif "3-" in mark:
        percent = 71
    elif "2+" in mark:
        percent = 68
    elif "2" in mark:
        percent = 65
    elif "2-" in mark:
        percent = 61
    elif "1" in mark:
        percent = 58
    elif "1" in mark:
        percent = 55
    elif "1" in mark:
        percent = 51
    elif "R" or "r" in mark:
        percent = 25

    return percent


def main():
    # This function gets the student's mark

    # Input
    mark = input("Enter the student's mark (ex. 4+): ")
    print(" ")

    # Call Functions
    percent = percent_convert(mark)

    print("The student's mark is {0}%".format(percent))


if __name__ == "__main__":
    main()
