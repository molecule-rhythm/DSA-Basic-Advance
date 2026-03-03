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

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     pop_value = self.tail.data
    #     if self.length == 1:
    #         self.head = None
    #         self.tail = None
    #     else:
    #         current = self.head
    #         while current.next:
    #             if current.next == self.tail:
    #                 current.next = None
    #                 self.tail = current
    #                 break
    #             current = current.next
    #     self.length -= 1
    #     return pop_value

    def pop(self):
        if self.length == 0:
            return None
        temp= self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.data

my_linked_list = LinkedList(10)
my_linked_list.append(20) 
my_linked_list.append(30)
my_linked_list.pop()
my_linked_list.print_list()  

# Output: 10 -> 20 -> 30 -> None