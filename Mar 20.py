#  Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

root = Node("Grand Parent")
parent1 = Node("Parent 1")
parent2 = Node("Parent 2")
parent3 = Node("Parent 3")

root.children.append(parent1)
root.children.append(parent2)
root.children.append(parent3)

parent1.children.append(Node("Child 1"))
parent1.children.append(Node("Child 2"))
parent2.children.append(Node("Child 3"))
parent3.children.append(Node("Child 4"))
parent3.children.append(Node("Child 5"))

print(f"Root Node: {root.data}")
print(f"Child nodes of root: {[child.data for child in root.children]}")
print(f"Child nodes of parent1: {[child.data for child in parent1.children]}")
print(f"Child nodes of parent2: {[child.data for child in parent2.children]}")
print(f"Child nodes of parent3: {[child.data for child in parent3.children]}")
