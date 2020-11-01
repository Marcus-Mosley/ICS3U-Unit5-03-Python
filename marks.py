#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on November 2020
# This program converts a student's mark into a percentage


def percent_convert(mark):
    # This function converts a student's mark into a percentage

    if mark == "4+":
        percent = 98
    elif mark == "4":
        percent = 91
    elif mark == "4-":
        percent = 83
    elif mark == "3+":
        percent = 78
    elif mark == "3":
        percent = 75
    elif mark == "3-":
        percent = 71
    elif mark == "2+":
        percent = 68
    elif mark == "2":
        percent = 65
    elif mark == "2-":
        percent = 61
    elif mark == "1+":
        percent = 58
    elif mark == "1":
        percent = 55
    elif mark == "1-":
        percent = 51
    elif mark == "R" or "r":
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
