class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None
N = int(input("Nhập N: "))
Nums = [int(x) for x in input(f"Nhập {N} phần tử số nguyên:").split()]
Head = Node()
Tail = Head
for num in Nums:
    newnode = Node(num)
    Tail.next = newnode
    Tail = Tail.next
def display(Head):    
    cur = Head.next
    while cur.next:
        print(cur.val, end= "->")
        cur = cur.next
    print (cur.val)
display(Head)
def chen_phan_tu(A,x):
    cur = A
    while cur.next.val < x:
        cur = cur.next
    next = cur.next
    cur.next = Node(x)
    cur = cur.next
    cur.next = next
# x = int(input("Nhập x: "))
# chen_phan_tu(Head,x)
# display(Head)
def loc_chan(Head):
    res = Node()
    cur_r = res
    cur = Head.next
    while cur:
        if cur.val%2 == 0 :
            cur_r.next = Node(cur.val)
            cur_r = cur_r.next
        cur = cur.next
    return res
display(loc_chan(Head))