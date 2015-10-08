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

def binary_search(liste, value, find_lower):
    low = 0
    high = len(liste)-1
    while low <= high:
        mid = (low + high) // 2
        if liste[mid] > value:
            high = mid-1
        elif liste[mid] < value:
            low = mid+1
        else:
            return liste[mid]
    if find_lower:
        if low != 0:
            return liste[low - 1]
        else:
            return liste[low]
    else:
        if high != len(liste) - 1:
            return liste[high + 1]
        else:
            return liste[high]

if __name__ == "__main__":
    liste = [1,2,5,6,7,8,9,10]
    print binary_search(liste, 11, False)



