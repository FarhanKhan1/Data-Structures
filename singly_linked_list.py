class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def get_data(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, value):
        temp = self.head

        while temp.next != None:
            temp = temp.next
        new_node = Node(value)
        temp.next = new_node
        self.tail = new_node
    
    def add_between(self, value, after=None, before=None):
        new_node = Node(value)
        temp = self.head
        temp_temp = temp
        if after:
            while temp.value != after or temp:
                temp = temp.next
            new_node = temp.next
            temp.next = new_node

            print(f"This is after condition {temp.value} and {temp_temp.value}")

        else:
            while temp.value != before or temp:
                temp_temp = temp
                temp = temp.next
            temp_temp.next = new_node
            new_node = temp_temp
            print(f"this is before condition: {temp_temp.value} and {temp.value}")
            

list_ = Linked_List()
list_.add_first(3)
list_.add_first(4)
list_.add_first(5)
list_.add_end(2)
list_.add_end(1)
list_.add_first(6)
list_.add_between(4.5, None ,2)
list_.get_data()
