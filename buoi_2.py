class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_List():
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        new_node.next = cur
        self.head = new_node
    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()
        
