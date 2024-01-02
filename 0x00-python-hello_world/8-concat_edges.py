#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.index("object-oriented"): str.index("object-oriented") + 27] + str[106:112] + str[:6])