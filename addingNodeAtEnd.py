class Node:
    def __init__ (self,data):
        self.data = data
        self.next =None

head = Node(45)

node2 = Node(98)
node3 = Node(3)

head.next = node2
node2.next = node3

new_node = Node(50)

if head is None:
    head = new_node

else:
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node

temp = head

while temp:
    print({temp.data})
    temp = temp.next

print('None')