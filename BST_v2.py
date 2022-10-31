# BST preorder, posorder and inorder
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
        elif key<= root.val:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root            
 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right) 

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right) 

def posorder(root):
    if root:
        posorder(root.left)
        posorder(root.right)
        print(root.val)  

def search(root, value):
    if(root.val == value):
        return value 
        
    if(root.val<value):
        search(root.right, value)

    if(root.val>value):
        search(root.left, value)    

def left_height(node):
    ht = 0
    while node:
        ht += 1
        node = node.left
    return ht

def right_height(node):
    ht = 0 
    while node:
        ht += 1
        node = node.right
    return ht

def TotalNodes(root):
    if(root == None):
        return 0

    lh = left_height(root)
    rh = right_height(root)

    if(lh == rh):
        return 2**lh - 1
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)


# BST preorder, posorder and inorder
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
        elif key<= root.val:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root            
 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right) 

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right) 

def posorder(root):
    if root:
        posorder(root.left)
        posorder(root.right)
        print(root.val)  

def search(root, value):
    if(root.val == value):
        return value 
        
    if(root.val<value):
        search(root.right, value)

    if(root.val>value):
        search(root.left, value)    

def left_height(node):
    ht = 0
    while node:
        ht += 1
        node = node.left
    return ht

def right_height(node):
    ht = 0 
    while node:
        ht += 1
        node = node.right
    return ht

def TotalNodes(root):
    if(root == None):
        return 0

    lh = left_height(root)
    rh = right_height(root)

    if(lh == rh):
        return 2**lh - 1
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)

root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 100)


print("Inorder traversal of the given tree")
inorder(root)

print("Pos order traversal of the given tree")
posorder(root)

print("Pre order traversal of the given tree")
preorder(root)
TotalNodes(root)