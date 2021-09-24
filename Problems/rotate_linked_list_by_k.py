class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def push(data, head_ref):
    node = Node(data)
    node.next = (head_ref)
    (head_ref) = node
    return head_ref

def print_list(node):
    while (node != None):
        print(node.data, end = ' ')
        node = node.next
        
def rotate(head, k):
    if not head:
        return head
    
    tmp = head
    len_ = 1
    
    while (tmp.next != None):
        tmp = tmp.next
        len_ += 1
    
    if k > len_:
        k = k % len_
        
    k = len_ - k
    
    if k == 0 or k == len_:
        return head
    
    current = head
    count = 1
    
    while (count < k and current != None):
        current = current.next
        count += 1
        
    if current == None:
        return head
    
    # current points to the kth node
    kthnode = current
 
    # Change next of last node to previous head
    tmp.next = head
 
    # Change head to (k+1)th node
    head = kthnode.next
 
    # Change next of kth node to None
    kthnode.next = None
 
    # Return the updated head pointer
    return head
    

# Create a list 10.20.30.40.50.60
head = None
for i in range(60, 0, -10):
    head = push(i, head)
    
# Print linked list
print_list(head)
# 10 20 30 40 50 60
updated_head = rotate(head, 2)
print_list(updated_head)
# 50 60 10 20 30 40 
