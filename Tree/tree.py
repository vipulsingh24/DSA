class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it")
            return self

        if self.left and target < self.data:
            return self.left.search(target)
       
        if self.right and target > self.data:
            return self.right.search(target)
       
        print("Value is not in a tree") 

    def traverse_preorder(self):
        print(self.data)
        
        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):        
        if self.left:
            self.left.traverse_inorder()

        print(self.data)

        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()

        if self.right:
            self.right.traverse_postorder()

        print(self.data)
 
class Tree:
    def __init__(self, root, name=""):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

   
    def traverse_preorder(self):
        return self.root.traverse_preorder()

    def traverse_inorder(self):
        return self.root.traverse_inorder()

    def traverse_postorder(self):
        return self.root.traverse_postorder()

node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(2)
node.left.right = Node(6)
node.right.left = Node(13)
node.right.right = Node(10000)


#print(node.right.data)
#print(node.right.right.data)


my_tree = Tree(node, "Vipul's Tree")
#print(my_tree.name)
#print(my_tree.root.left.data)
#print(my_tree.root.right.data)
#found = my_tree.search(13)
#print(found.data)

# Traverse
tree = Tree(Node(50), "Tree Traversals")
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)

print("Pre-Order: ")
tree.traverse_preorder()
print("In-Order: ")
tree.traverse_inorder()
print("Post-Order: ")
tree.traverse_postorder()












