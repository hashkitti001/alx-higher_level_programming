#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldig = number % 10
if(ldig > 5):
    print("Last digit of", number, "is", ldig, "and is greater than 5\n")
elif(ldig == 0):
    print("Last digit of", number, "is", ldig, "and is greater than 0\n")
elif(ldig < 6 and ldig != 0):
    print("Last digit of", number, "is", ldig, "and is less
          than 6 and not 0\n")
