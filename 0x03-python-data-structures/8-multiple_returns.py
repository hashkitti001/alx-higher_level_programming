#!/usr/bin/python3
def multiple_returns(sentence):
    result_tuple = ()
    if len(sentence) == 0:
        return (None, "")
    return (len(sentence), sentence[0])
