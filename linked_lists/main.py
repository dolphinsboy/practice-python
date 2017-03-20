#!/usr/bin/env python

from linked_list import LinkedList
from node import Node

def main():
    link = LinkedList()
    head = Node(1)
    link.set_head(head)

    link.push(2)
    link.push(3)
    link.push(4)
    link.push(0)
    link.append(6)
    link.append(7)

    print len(link)
    print link

    link.delete(7)
    print link
    link.delete(6)
    print link

    link.append(5)
    print link
    print link.contains(5)
    print link.contains("5")

    for i in range(0, len(link)):
        print link
        link.pop()


main()
