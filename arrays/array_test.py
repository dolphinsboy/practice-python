#!/usr/bin/env python

def array_test():
    arr = [1, 2, 3, 4, 5]

    arr.pop()
    arr.append(6)

    print arr
    print "Index of 4: ",arr.index(4)

    arr.reverse()
    print arr

    arr.sort()
    print arr

array_test()
