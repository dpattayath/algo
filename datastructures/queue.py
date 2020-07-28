

# FIFO
class Queue():
    def __init__(self):
        self.stream = []

    def enqueue(self, data):
        self.stream.append(data)

    def dequeue(self):
        return self.stream.pop(0)

if __name__ == "__main__":
    myqueue = Queue()
    myqueue.enqueue(5)
    myqueue.enqueue(6)
    myqueue.enqueue(10)
    print(myqueue.dequeue())
    myqueue.enqueue(2)
    myqueue.enqueue(9)
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
