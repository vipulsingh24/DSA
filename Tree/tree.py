class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

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

    def height(self, h=0):
        left_height = self.left.height(h+1) if self.left else h
        right_height = self.right.height(h+1) if self.right else h
        return max(left_height, right_height)

    def get_nodes_at_depth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None] * 2 **(depth-1))

        if self.right:
            self.right.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None] * 2 **(depth-1))

        return nodes

    def add(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def delete(self, target):
        if self.data == target:
            if self.left and self.right:
                # RTFM (Right tree find minimum)
                min_value = self.right.find_min()
                self.data = min_value
                self.right = self.right.delete(min_value)
                return self
            else:
                return self.left or self.right
       
        if self.right and target > self.data:
            self.right = self.right.delete(target)
        if self.left and target < self.data:
            self.left = self.left.delete(target)
        return self
 
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

    def height(self):
        return self.root.height()

    def get_nodes_at_depth(self, depth):
        return self.root.get_nodes_at_depth(depth)

    def _node_to_char(self, n, spacing):
        if n is None:
            return "_" + (" "*spacing)
        spacing = spacing - len(str(n)) + 1
        return str(n) + (" "* spacing)

    def print_tree(self, label=""):
        print(self.name + " " + label)
        height = self.root.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing - 1) + 1)
        offset = int((width - 1) / 2)
 
        for depth in range(0, height - 1):
            if depth > 0:
                print("  " * (offset - 1) + (" " * (spacing + 2)).join(["/" + (" " * (spacing - 2)) + "\\"] * (2 ** (depth - 1))))
            row = self.root.get_nodes_at_depth(depth, [])
            print((" " * offset) + "".join([self._node_to_char(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1
        print("")

    def add(self, data):
        self.root.add(data)

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
tree.root.left.left.left.left = Node(2)

print("Pre-Order: ")
tree.traverse_preorder()
print("In-Order: ")
tree.traverse_inorder()
print("Post-Order: ")
tree.traverse_postorder()


# print(tree.root.height())
print("Height: ", tree.height())
print(tree.get_nodes_at_depth(4))
tree.print_tree()









