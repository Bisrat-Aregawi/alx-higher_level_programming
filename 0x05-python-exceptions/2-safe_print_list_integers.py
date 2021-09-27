#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count, printed = 0, 0
    for elem in my_list:
        count += 1

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except ValueError:
            pass
    print("")

    return (printed)
