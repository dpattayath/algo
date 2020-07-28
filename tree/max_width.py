
from binary_tree import BinaryTree

def level_order(node, level, queue):
    if not node:
        return
    if level == 1:
        print(node.data, end=", ")
    else:
        level_order(node.left, level - 1, queue)
        level_order(node.right, level - 1, queue)


def height(node):
    if not node:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def get_width(root,level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return (get_width(root.left, level - 1) + get_width(root.right, level - 1))

"""
level walkthrough with recursion
"""
def get_max_width(root):
    maxWidth = 0
    h = height(root)
    for i in range(1, h + 1):
        width = get_width(root, i)
        if (width > maxWidth):
            maxWidth = width
    return maxWidth

"""
level walkthrough with queue
"""
def get_max_width_queue(root):
    if root is None:
        return 0

    queue = [root]
    max_width = 0

    while (len(queue) > 0):
        count = len(queue)
        max_width = max(count, max_width)

        while count > 0:
            node = queue.pop(0)
            count -= 1

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return max_width

if __name__ == "__main__":
    mytree = BinaryTree()
    mytree.insert(10)
    mytree.insert(8)
    mytree.insert(5)
    mytree.insert(7)
    mytree.insert(2)
    mytree.insert(12)
    mytree.insert(15)
    mytree.insert(11)
    # mytree.pre_order()
    print(get_max_width(mytree.root))
    print(get_max_width_queue(mytree.root))
