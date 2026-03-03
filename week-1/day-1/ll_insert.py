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
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    # def insert(self,index,value):
    #     if index < 0 or index > self.length:
    #         return False
    #     new_node = Node(value)
    #     if index == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #         current = self.head
    #         for _ in range(index - 1):
    #             current = current.next
    #         new_node.next = current.next
    #         current.next = new_node
    #     self.length += 1
    #     return True

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

my_linked_list = LinkedList(10)
my_linked_list.append(20) 
my_linked_list.append(30)
my_linked_list.insert(3, 50)
my_linked_list.insert(4, 30)
my_linked_list.print_list() 