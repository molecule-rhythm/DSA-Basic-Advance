class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
       

    # def print_list(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")

    def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            return True

    def middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.data
    
my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(50)
print(my_linked_list.middle_node())  # Output: 30
my_linked_list.append(60)
print(my_linked_list.middle_node())  # Output: 40
# print(my_linked_list.print_list())  # Output: 40
