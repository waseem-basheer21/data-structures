class Node:
    def __init__ (self,data):
        self.data = data
        self.next  =None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head = new_node
       
    def insert_at_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_data(self,target,new_data):
        new_node = Node(new_data)

        current = self.head

        while current:
            if current.data == target:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def display(self):
        current = self.head
        if current is None:
            print("Linked List is empty")
            return
        print ("Linked List: ", end="")
        
        while current:

            print(f"{current.data} ->" , end="")
            current = current.next
        print("None")


    def delete_at_beginning(self):
        if self.head is None:
            print("Deletion Failed: List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Deletion Failed: List is empty")
            return
        current = self.head

        while current.next.next:
            current = current.next
        current.next = None

    def delete_by_data(self,target):
        current = self.head
        prev = None
        while current and current.data != target:
            prev = current
            current = current.next
        prev.next = current.next

        

    

my_list = LinkedList()

my_list.insert_at_beginning(60)
my_list.insert_at_end(50)
my_list.insert_after_data(60,30)
# my_list.delete_at_beginning()
my_list.delete_by_data(30)

my_list.display()