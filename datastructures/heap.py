"""
Min Heap has the mininmum element at the root and increasing on the way down.
Adding an element to heap is followed by adding to the next possible slot and bubbling way up to the righ spot.
Deleting the min element involves removing the root, swapping it with the leaf element and bubble the way down.

Best data structure to store and visualize this is an array with:

    left node = index * 2 + 1
    right node = index * 2 + 2
    parent node = (index - 2) / 2

"""

class Heap():
    def __init__(self, is_max=False):
        self.data = []
        self.is_max = is_max

    def get_left_index(self, index):
        return index * 2 + 1

    def get_right_index(self, index):
        return index * 2 + 2

    def get_parent_index(self, index):
        return int((index - 2) / 2)

    def has_left_node(self, index):
        return self.get_left_index(index) < len(self.data)

    def has_right_node(self, index):
        return self.get_right_index(index) < len(self.data)

    def has_parent_node(self, index):
        return self.get_parent_index(index) >= 0

    def get_left_node(self, index):
        return self.data[self.get_left_index(index)]

    def get_right_node(self, index):
        return self.data[self.get_right_index(index)]

    def get_parent_node(self, index):
        return self.data[self.get_parent_index(index)]

    def add(self, data):
        self.data.append(data)
        self.heapify_up()

    def peek(self):
        return self.data[0]

    def pop(self):
        value = self.data.pop()
        to_pop = self.data[0]
        self.data[0] = value
        self.heapify_down()
        return to_pop

    def comparator(self, index1, index2):
        if self.is_max:
            return self.data[index1] < self.data[index2]
        else:
            return self.data[index1] > self.data[index2]

    def heapify_up(self):
        index = len(self.data) - 1
        while self.has_parent_node(index) and self.comparator(self.get_parent_index(index), index):
            parent_index = self.get_parent_index(index)
            self.data[parent_index], self.data[index] = self.data[index], self.data[parent_index]
            index = parent_index

    def heapify_down(self):
        index = 0
        while self.has_left_node(index):
            left_index = self.get_left_index(index)
            right_index = self.get_right_index(index)

            smaller_child_index = left_index
            if self.has_right_node(index) and self.data[right_index] < self.data[left_index]:
                smaller_child_index = right_index

            if self.comparator(smaller_child_index, index):
                break
            else:
                self.data[index], self.data[smaller_child_index] = self.data[smaller_child_index], self.data[index]

            index = smaller_child_index

    def size(self):
        return len(self.data)

    def print(self):
        print(self.data)


if __name__ == "__main__":
    myheap = Heap(is_max=False)
    myheap.add(10)
    myheap.add(15)
    myheap.add(20)
    myheap.add(17)
    myheap.print()
    myheap.pop()
    myheap.print()
    myheap.add(25)
    myheap.print()
