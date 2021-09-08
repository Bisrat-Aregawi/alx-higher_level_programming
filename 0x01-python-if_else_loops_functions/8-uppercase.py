#!/usr/bin/python3
def uppercase(str):
    asci = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            asci = ord(i) - 32
        else:
            asci = ord(i)
        print("{:c}".format(asci), end="")
    print("")
