
from binary_tree import BinaryTree

"""
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Given a binary tree, print the top view of it. The output nodes can be printed in any order.
Expected time complexity is O(n)
A node x is there in output if x is the topmost node at its horizontal distance.
Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and
that of right child is horizontal distance of x plus 1.
"""

def top_view(root):
    if(root == None) :
        return

    q = []
    m = dict()
    level = 0
    root.level = level

    # push node and horizontal
    # distance to queue
    q.append(root)

    while(len(q)) :
        node = q[0]
        level = node.level

        # count function returns 1 if the
        # container contains an element
        # whose key is equivalent to level,
        # or returns zero otherwise.
        if level not in m:
            m[level] = node.data
        if(node.left):
            node.left.level = level - 1
            q.append(node.left)
        if(node.right):
            node.right.level = level + 1
            q.append(node.right)

        q.pop(0)

    for i in sorted(m):
        print(m[i], end=" ")

if __name__ == "__main__":
    mytree = BinaryTree()
    mytree.insert(10)
    mytree.insert(5)
    mytree.insert(7)
    mytree.insert(2)
    mytree.insert(8)

    top_view(mytree.root)

