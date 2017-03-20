from node import Node

class LinkedList:

    def __init__(self):
        self.head_ = None

    def set_head(self, node):
        self.head_ = node

    def __len__(self):
        count = 0
        current = self.head_
        while current:
            current = current.get_next()
            count += 1
        return count

    def __str__(self):
        current = self.head_
        output = ""

        while current:
            if current.get_next():
                output += str(current) + "->"
            else:
                output += str(current)
            current = current.get_next()
        return output

    def push(self, value):
        node = Node(value)

        if self.head_:
            node.set_next(self.head_)
            self.head_ = node
        else:
            self.set_head(node)

    def append(self, value):
        node = Node(value)
        current = self.head_

        while current.get_next():
            current = current.get_next()
        current.set_next(node)

    def delete(self, value):
        if not self.head_:
            raise IndexError, "Empty list"
        else:
            if self.head_.get_data() == value:
                self.head_ = self.head_.get_next()
            else:
                prev = self.head_
                current = prev
                while current.get_next():
                    current = current.get_next()

                    if current.get_data() == value:
                        prev.set_next(current.get_next())
                    else:
                        prev = current

    def pop(self):
        if self.head_:
            self.head_ = self.head_.get_next()
        else:
            raise IndexError,"Empty list"

    def contains(self, value):
        current = self.head_

        while current:
            if current.get_data() == value:
                return True
            else:
                current = current.get_next()
        return False






