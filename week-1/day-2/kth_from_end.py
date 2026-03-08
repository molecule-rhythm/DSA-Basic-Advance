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

    def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def kth_from_end(self, k):
        if k < 0 or k >= self.length:
            return None
        
        slow = self.head
        fast = self.head
        
        for _ in range(k):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        return slow.data
my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
print(my_linked_list.kth_from_end(0))  # Output: 30
print(my_linked_list.kth_from_end(1))  # Output: 20
print(my_linked_list.kth_from_end(2))  # Output: 10
print(my_linked_list.kth_from_end(3))  # Output: None (k is out of bounds)