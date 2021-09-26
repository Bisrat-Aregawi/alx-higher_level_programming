#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count, printed = 0, 0
    for i in my_list:
        count += 1
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:
        print("")
        quit()
    print("")
    return printed
