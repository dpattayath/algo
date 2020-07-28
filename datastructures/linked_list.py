
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def print_forward(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def print_backward(self):
        node = self.tail
        while node:
            print(node.data)
            node = node.prev

if __name__ == "__main__":
    mylist = LinkedList()
    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    mylist.print_forward()
    mylist.print_backward()
