
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0

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


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        queue = [self.root]

        while len(queue) > 0:
            node = queue[0]
            if not node.left:
                node.left = Node(data)
                break
            elif not node.right:
                node.right = Node(data)
                break
            else:
                queue.append(node.left)
                queue.append(node.right)

            queue.pop(0)

    def in_order(self):
        self.root.in_order()

    def pre_order(self):
        self.root.pre_order()

    def post_order(self):
        self.root.post_order()

    def level_order(self):
        self.root.level_order()

if __name__ == "__main__":
    mytree = BinaryTree()
    mytree.insert(1)
    mytree.insert(2)
    mytree.insert(3)
    mytree.insert(4)
    mytree.insert(5)
    mytree.insert(6)
    mytree.insert(7)
    mytree.pre_order()
