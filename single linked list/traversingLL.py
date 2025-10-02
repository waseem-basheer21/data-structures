class Node:
    def __init__ (self,data):
        self.data = data
        self.next =None

head = Node(45)

node2 = Node(98)
node3 = Node(3)

head.next = node2
node2.next = node3

current_node = head

while current_node:
    print({current_node.data})
    current_node = current_node.next
print("None")

