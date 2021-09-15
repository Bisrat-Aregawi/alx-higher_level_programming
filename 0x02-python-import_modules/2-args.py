#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    n = len(sys.argv)
    if n > 0:
        for i in range(1, n):
            print("{:d}: {:s}".format(i, sys.argv[i]))
