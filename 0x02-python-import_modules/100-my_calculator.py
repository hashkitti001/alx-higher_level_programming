#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    allowed_ops_dict = {"+" : add , "-": sub, "*": mul, "/": div}
    if (argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    elif (sys.argv[2] not in allowed_ops_dict):
          print("Unknown operator. Available operators: +, -, * and /")
          sys.exit(1)
    else:
         a = int(sys.argv[1])
         b = int(sys.argv[3])
         print("{} {} {} = {}".format(a, sys.argv[2], b, allowed_ops_dict[sys.argv[2]](a, b)))
