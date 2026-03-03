
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    
    def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def get(self, index):
            if index < 0 or index >= self.length:
                return None
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data

    def set_value(self,index,value):
        if index < 0 or index >= self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value
        return value
    
my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.print_list()  
print(my_linked_list.set_value(0,2))  # Output: 10
print(my_linked_list.set_value(1,3))  # Output: 20
print(my_linked_list.set_value(2,4))  # Output: 30
print(my_linked_list.set_value(3,5))  # Output: None
my_linked_list.print_list()  
