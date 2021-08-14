class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root, path=""):
    """
     Root -> Left -> Right
    """
    if root:
        path += str(root.data) + "-"
        path = preorder(root.left, path)
        path = preorder(root.right, path)
    return path


def inorder(root, path=""):
    """
     Left -> Root -> Right
    """
    if root:
        path = inorder(root.left, path)
        path += str(root.data) + "-"
        path = inorder(root.right, path)
    return path


def postorder(root, path=""):
    """
     Left -> Right -> Root
    """
    if root:
        path = postorder(root.left, path)
        path = postorder(root.right, path)
        path += str(root.data) + "-"
    return path


if __name__ == "__main__":
    root = Node("F")
    root.left = Node("D")
    root.left.left = Node("B")
    root.left.left.left = Node("A")
    root.left.left.right = Node("C")
    root.left.right = Node("E")
    root.right = Node("I")
    root.right.left = Node("G")
    root.right.left.right = Node("H")
    root.right.right = Node("J	")

    print("Preorder: ", preorder(root))
    print("Postorder: ", postorder(root))
    print("Inorder: ", inorder(root))














