class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def set_next(self, next):
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next
