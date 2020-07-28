
# LIFO
class Stack():
    def __init__(self):
        self.stream = []

    def push(self, data):
        self.stream.append(data)

    def pop(self):
        return self.stream.pop()

if __name__ == "__main__":
    mystack = Stack()
    mystack.push(5)
    mystack.push(6)
    mystack.push(10)
    print(mystack.pop())
    mystack.push(2)
    mystack.push(9)
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
