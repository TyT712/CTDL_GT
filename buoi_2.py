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
        while cur.next:
            print(cur.data, end="->")
            cur = cur.next
        print(cur.data)  # Print the last node's data
    def pop(self):
        if not self.head:
            print("Danh sách rỗng")
            return
        cur = self.head
        self.head = cur.next
        del cur
    def search(self):
        return

A = Linked_List()
A.insert(5)
A.insert(2)
A.insert(7)
A.insert(8)
A.insert(6)
A.insert(3)
A.insert(10)
A.display()
# Indicate the end of the list
cur = A.head
def loc_chan(cur):
    if cur is None:
        return
    cur.next = loc_chan(cur.next)
    if cur.data % 2 == 0:
        return cur
    return cur.next
B = Linked_List()
B.head = loc_chan(cur)
B.display()

head : Node = None
def add_node(head,data):
    if head is None:
        return Node(data)
    head.next = add_node(head.next, data)
    return head
head = add_node(head, 5)
head = add_node(head, 2)
head = add_node(head, 7)
def display(head):
    if head is None:
        return
    print(head.data, end="->")
    display(head.next)
display(head)
