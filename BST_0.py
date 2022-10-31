# Binary Search Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)

    else:
        if root.val == key:
            return root
        elif root.val <= key:
             root.right = insert(root.right, key)
        else:
             root.left = insert(root.left, key)
    return root 

def search(root, value):
    if root.val == value:
        return root

    if root.val < value:
        return search(root.right, value)

    if root.val > value:
        return search(root.left, value)                              

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right) 

def minValueNode(node):
    current = node

    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return None

    if key < root.val:
        root.left = deleteNode(root.left,key)

    elif key>root.val:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.val = temp.key
        root.right = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root    

root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the given tree")
inorder(root)