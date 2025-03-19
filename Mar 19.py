# Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

root  = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

child1.children.append(Node(5))
child3.children.append(Node(6))

print(f"Root Node: {root.data}")
print(f"Child nodes of root: {[child.data for child in root.children]}")
print(f"Child nodes of child1: {[child.data for child in child1.children]}")
print(f"Child nodes of child3: {[child.data for child in child3.children]}")
