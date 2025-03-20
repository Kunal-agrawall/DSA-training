# Tree

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

# root = Node("Grand Parent")
# parent1 = Node("Parent 1")
# parent2 = Node("Parent 2")
# parent3 = Node("Parent 3")

# root.children.append(parent1)
# root.children.append(parent2)
# root.children.append(parent3)

# parent1.children.append(Node("Child 1"))
# parent1.children.append(Node("Child 2"))
# parent2.children.append(Node("Child 3"))
# parent3.children.append(Node("Child 4"))
# parent3.children.append(Node("Child 5"))

# print(f"Root Node: {root.data}")
# print(f"Child nodes of root: {[child.data for child in root.children]}")
# print(f"Child nodes of parent1: {[child.data for child in parent1.children]}")
# print(f"Child nodes of parent2: {[child.data for child in parent2.children]}")
# print(f"Child nodes of parent3: {[child.data for child in parent3.children]}")

# ////////////////////////////////////////////////////////////////////////////////////////////

# Tree

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

# root = Node("CEO")
# manager1 = Node("Manager1")
# manager2 = Node("Manager2")
# manager3 = Node("Manager3")

# root.children.append(manager1)
# root.children.append(manager2)
# root.children.append(manager3)

# manager1.children.append(Node("Employee1"))
# manager1.children.append(Node("Employee2"))
# manager2.children.append(Node("Employee3"))
# manager3.children.append(Node("Employee4"))

# print(f"Root Node: {root.data}")
# print(f"Employees of CEO: {[employee.data for employee in root.children]}")
# print(f"Employees of Manager1: {[employee.data for employee in manager1.children]}")
# print(f"Employees of Manager2: {[employee.data for employee in manager2.children]}")
# print(f"Employees of Manager3: {[employee.data for employee in manager3.children]}")

# //////////////////////////////////////////////////////////////////////////


class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

root = Node(1)
child1 = Node(2)
root.children.append(child1)
child1.children.append(Node(5))
child1.children.append(Node(6))

child2  = Node(3)
root.children.append(child2)

child3 = Node(4)
root.children.append(child3)
child3.children.append(Node(7))

print(f"Root Node: {root.data}")
print(f"Child Node of 1: {child1.data}")
