#!/usr/bin/env python

from merge_sort import MergeSort

def main():
    numbers = [3,4,1,2,10,9,8]
    m = MergeSort(numbers)
    m.sort()

    print numbers

main()

