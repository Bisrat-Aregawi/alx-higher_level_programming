#!/usr/bin/python3
i, j = 122, 26
while j > 0:
    if i == 122:
        print("{:c}".format(i), end="")
        j, i = j - 1, i - 1
        continue
    if i+1 >= 97 and i+1 <= 122:
        i = i-32
    elif i+1 >= 65 and i+1 <= 97:
        i = i+32
    print("{:c}".format(i), end="")
    j, i = j-1, i-1
