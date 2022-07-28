"""
Finding the sum of all the nodes in a binary tree
"""

# Binary tree node


class newNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def addRoot(root):

    q = []
    
    q.append(root)

    sum = 0

    while len(q) > 0:
        temp = q.pop(0)
        print(temp.key)

        sum += temp.key

        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right) 

    return sum

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.left.left.left = newNode(8)

    print("Sum of the values in the tree is -> ", addRoot(root))
    
        
