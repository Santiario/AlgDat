__author__ = 'Vemund'


class Node:

    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


def tree_maximum(node):
    while node.right != None:
        node = node.right
    return node


def tree_minimum(node):
    while node.left != None:
        node = node.left
    return node


def successor(node):
    if node.right:
        return tree_minimum(node.right)
    suc = node.parent
    while suc and suc.right == node:
        node = suc
        suc = suc.parent
    return suc


def predecessor(node):
    if node.left:
        return tree_maximum(node.left)
    pre = node.parent
    while node.parent and pre.left == node:
        node = pre
        pre = node.parent  # Kunne ogsaa vert pre = pre.parent
    return pre


if __name__ == "__main__":
    pass



