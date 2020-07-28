
from binary_tree import BinaryTree

def vertical_sum(root):
    if not root:
        return

    q = []
    level = 0
    mapper = {}

    root.level = level
    mapper[level] = root.data
    q.append(root)

    while len(q) > 0:
        node = q[0]
        level = node.level

        if node.left:
            node.left.level = level - 1
            mapper[node.left.level] = mapper.get(node.left.level, 0) + node.left.data
            q.append(node.left)

        if node.right:
            node.right.level = level + 1
            mapper[node.right.level] = mapper.get(node.right.level, 0) + node.right.data
            q.append(node.right)

        q.pop(0)

    print(mapper)

if __name__ == "__main__":
    mytree = BinaryTree()
    mytree.insert(1)
    mytree.insert(2)
    mytree.insert(3)
    mytree.insert(4)
    mytree.insert(5)
    mytree.insert(7)
    mytree.insert(6)
    # mytree.pre_order()
    vertical_sum(mytree.root)
