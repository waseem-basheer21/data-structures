class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head

        while current.next !=self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_after_data(self,target,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.data != target:
            current = current.next
            if current == self.head:  
                print("Target not found!")
                return
        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        new_node.next = new_node

        current = self.head

        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        return
    
    def display(self):
        current = self.head

        while current:
            print(f"{current.data}-> ", end="")
            current = current.next
            if current == self.head:
                break
        
        print("...")

    def delete_at_beginning(self):
        if self.head is None:
            return
        
        # If only one node is present
        if self.head == self.head.next:
            self.head = None
            return

        last = self.head

        while last.next != self.head:
            last = last.next
        self.head = self.head.next
        last.next = self.head

        

    def delete_at_end(self):
        if self.head is None:
            return
        # if only one node is present
        if self.head == self.head.next:
            self.head = None
            return
        
        last = self.head

        while last.next.next != self.head:
            last = last.next
        
        last.next = self.head

    def delete_at_specific_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos <= 0:
            print("Invalid position")
            return

        # Deleting head
        if pos == 1:
            if self.head.next == self.head:
                self.head = None
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return

        current = self.head
        prev = None
        count = 1
        while count < pos and current.next != self.head:
            prev = current
            current = current.next
            count += 1

        if count != pos:
            print("Position out of range")
            return

        prev.next = current.next
        current = None


my_list = Circular_linked_list()

my_list.insert_at_beginning(23)
my_list.insert_after_data(23,24)
my_list.insert_after_data(24,25)
my_list.insert_at_end(26)
# my_list.delete_at_beginning()
# my_list.delete_at_end()
# my_list.delete_at_specific_pos()
my_list.display()

