class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Create the nodes and set node1 as head
head = node1

head = Node(45)
node2 = Node(98)
node3 = Node(3)

# Link the nodes starting from head

head.next = node2
node2.next = node3
