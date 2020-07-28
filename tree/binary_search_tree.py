
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0

    def insert(self, data):
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)

    def print_level(self, node, level):
        if not node:
            return
        if level == 1:
            print(node.data, end=", ")
        else:
            self.print_level(node.left, level - 1)
            self.print_level(node.right, level - 1)

    def height(self, node):
        if not node:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def level_order(self):
        h = self.height(self)
        for i in range(1, h + 1):
            self.print_level(self, i)

    def __repr__(self):
        return str(self.data)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def in_order(self):
        self.root.in_order()

    def pre_order(self):
        self.root.pre_order()

    def post_order(self):
        self.root.post_order()

    def level_order(self):
        self.root.level_order()

def is_binary_search_tree(node, min_val, max_val):
    if not node:
        return True
    if node.data < min_val or node.data > max_val:
        return False
    else:
        return is_binary_search_tree(node.left, min_val, node.data - 1) and is_binary_search_tree(node.right, node.data + 1, max_val)

if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree.insert(10)
    mytree.insert(5)
    mytree.insert(7)
    mytree.insert(2)
    mytree.insert(8)
    mytree.in_order()
    print("------")
    mytree.pre_order()
    print("------")
    mytree.post_order()
    print("------")
    mytree.level_order()
    print(is_binary_search_tree(mytree.root, float('-inf'), float('inf')))
