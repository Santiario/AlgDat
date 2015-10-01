__author__ = 'Vemund'

class Vertex:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False



def print_path(source, target):
    if target == source:
        print 'The shortest path is:', source,
    elif target.parent is None:
        print 'No path from', source, 'to', target, 'exists'
    else:
        print_path(source, target.parent)
        print target,

node1 = Vertex('a')
node2 = Vertex('b', node1)
node3 = Vertex('c', node1)
node4 = Vertex('d', node2)

print_path(node1, node4)
