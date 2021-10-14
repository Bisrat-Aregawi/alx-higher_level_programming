#!/usr/bin/python3
"""Module parses arguments to it and performs calculations.

It imports the module 'calculator_1.py', validates the the usage (which should
be only two numbers and one operator), performs calculations using functions
from the imported module and prints to stdout the annotations with the result.
It also exits with status codes 1 and 0, where 1 is for useage error and 0 for
a error free computation.
"""


if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    operators = ['+', '-', '*', '/']

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    arg1, arg2 = sys.argv[1], sys.argv[3]

    if (sys.argv[2] in operators):
        if sys.argv[2] == '+':
            print(f"{arg1} + {arg2} = {calc.add(int(arg1), int(arg2))}")
        elif sys.argv[2] == '-':
            print(f"{arg1} - {arg2} = {calc.sub(int(arg1), int(arg2))}")
        elif sys.argv[2] == '*':
            print(f"{arg1} * {arg2} = {calc.mul(int(arg1), int(arg2))}")
        elif sys.argv[2] == '/':
            print(f"{arg1} / {arg2} = {calc.div(int(arg1), int(arg2))}")
        sys.exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
