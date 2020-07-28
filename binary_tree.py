"""
Balance Binary search tree - O(log n) for search and insert
In-order traversal
search
insert
"""

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if not self.left:
                return False
            return self.left.contains(value)
        else:
            if not self.right:
                return False
            return self.right.contains(value)

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.data)
        if self.right:
            self.right.printInOrder()

if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(5)
    n3 = Node(10)
    n4 = Node(2)
    n5 = Node(6)
    n6 = Node(8)

    n1.left = n2
    n1.right = n3
    n2.left = n4

    n1.printInOrder()
    n1.insert(8)
    n1.insert(5)
    n1.printInOrder()
    print(n1.contains(11))
