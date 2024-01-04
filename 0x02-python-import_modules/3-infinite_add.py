#!/usr/bin/python3
import sys
if __name__ == "__main__":
   int_args = []
   for arg in sys.argv[1:]:
       int_args.append(int(arg))
print(sum(int_args))
