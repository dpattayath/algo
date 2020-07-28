from ds.heap import Heap


class Solution():
    def __init__(self):
        self.lowers = Heap(is_max=True) # max heap for lower half
        self.highers = Heap(is_max=False) # min heap for higher half

    def get_medians(self, source):
        medians = []
        for item in source:
            self.add_item(item)
            self.rebalance()
            medians.append(self.get_median())
        return medians

    def add_item(self, item):
        if self.lowers.size() == 0 or item < self.lowers.peek():
            self.lowers.add(item)
        else:
            self.highers.add(item)

    def rebalance(self):
        bigger_heap = self.lowers if self.lowers.size() > self.highers.size() else self.highers
        smaller_heap = self.highers if self.lowers.size() > self.highers.size() else self.lowers

        if bigger_heap.size() - smaller_heap.size() >= 2:
            smaller_heap.add(bigger_heap.pop())

    def get_median(self):
        bigger_heap = self.lowers if self.lowers.size() > self.highers.size() else self.highers
        smaller_heap = self.highers if self.lowers.size() > self.highers.size() else self.lowers

        if bigger_heap.size() == smaller_heap.size():
            return (bigger_heap.peek() + smaller_heap.peek()) / 2
        else:
            return bigger_heap.peek()


if __name__ == "__main__":
    mysol = Solution()
    print(mysol.get_medians([1,2,3,4,5,6,7,8,9,10]))

