from Node import Node


a = Node(4)
b = Node(4)
c = Node(4)

a.add_child(b)
a.add_child(c)

print(a.children)

for child in a.children:
    print(child.data)