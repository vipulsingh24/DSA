class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
        
def get_height(root):
    if root.left == None or root.right == None:
        return 0
    
    left = 0
    if root.left:
        left = get_height(root.left)
        
    right = 0
    if root.right:
        right = get_height(root.right)
        
    return max(left, right) + 1


def calculate_level_sum(node, level):
    global sum_
    
    if node == None:
        return
    
    sum_[level] += node.data
    calculate_level_sum(node.left, level+1)
    calculate_level_sum(node.right, level+1)
    

root = Node(6)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)



levels = get_height(root) + 1
sum_ = [0] * levels
calculate_level_sum(root, 0)
print(sum_)  # [[6, 12, 24]
