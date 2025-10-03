class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_linked_list:
    def __init__ (self):
        self.head = None
    
    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        new_node.next = None

    def insert_at_specific_pos(self,pos,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        prev = None
        current = self.head
        count = 1

        if pos <= 0:
            print("please select from 1 onwards")
            return
        
        if pos == 1:
            self.insert_at_beginning(new_data)
            return
        
        
        while current  and count < pos:
            prev = current
            count +=1
            current = current.next

        prev.next = new_node
        new_node.prev = prev
        new_node.next = current
        current.prev = new_node
    

    def delete_at_beginning(self):
        if self.head is None:
            print("Failed to delete, Linked list is empty...")
            return
        
        self.head = self.head.next
        self.head.next.prev = None
        return

    def delete_at_end(self):
        if self.head is None:
            print("Linked list empty..")
            return
        
        last = self.head

        while last.next:
            last = last.next
        
        last.prev.next = None
        return

    def delete_at_specific_pos(self,pos):
        if self.head is None:
            print("Linked list is empty...")
            return

        current  =self.head
        count = 1

        if pos <=0:
            print("Invalid position...")
            return
        
        if pos == 1:
            self.delete_at_beginning()
            return

        while current and count < pos:
            count += 1
            current = current.next
        
        if current is None:
            print("Position out of range...")
            return

        if current.next.next is None:
            self.delete_at_end()
            return

        current.prev.next = current.next
        current.next.prev = current.prev
        


    def display(self):
        current = self.head

        while current:
            print(f" <-{current.data}->" , end="")
            current = current.next
        print("end of list")

my_list = Double_linked_list()
my_list.insert_at_beginning(23)
my_list.insert_at_beginning(24)
my_list.insert_at_end(25)
my_list.insert_at_specific_pos(3,29)
my_list.insert_at_specific_pos(4,39)
# my_list.delete_at_beginning()
# my_list.delete_at_end()
my_list.delete_at_specific_pos(4)
my_list.display()