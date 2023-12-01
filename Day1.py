# Advent of Code day 1: read text, identify number from string, parse first digit and last digit, total sum

import numpy as np

# Read text:
pathname = "C:\\Users\\arobinso\\OneDrive - ANSYS, Inc\\Documents\\Advancement\\Advent of Code\\Day1.txt"
f = open(pathname, 'r')

total_sum = 0
for line in f:
    digit_array = []
    print(line)
    if "one" in line:
        line = line.replace("one", 'o1e')
    if "two" in line:
        line = line.replace("two", 't2o')
    if "three" in line:
        line = line.replace("three", 't3e')
    if "four" in line:
        line = line.replace("four", 'f4r')
    if "five" in line:
        line = line.replace("five", 'f5e')
    if "six" in line:
        line = line.replace("six", 's6x')
    if "seven" in line:
        line = line.replace("seven", 's7n')
    if "eight" in line:
        line = line.replace("eight", 'e8t')
    if "nine" in line:
        line = line.replace("nine", 'n9e')
    print(line)
    # check digits
    for n in line:
        if n.isnumeric():
            digit_array.append(int(n))

    first = str(digit_array[0])
    last = str(digit_array[-1])
    total = int(first + last)
    print(total)
    total_sum = total_sum + total
print(total_sum)
