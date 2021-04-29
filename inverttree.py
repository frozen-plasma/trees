class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createbst(lis):
    s_lis = sorted(lis)
    root = r_cb(s_lis)
    return root

def r_cb(lis):
    mid = int(len(lis)/2)
    if not lis:
        return None
    root = Node(lis[mid])
    root.left = r_cb(lis[0:mid])
    root.right = r_cb(lis[mid+1:len(lis)])
    return root

def printtree(root):
    if root:

        printtree(root.left)
        print(root.val)
        printtree(root.right)

def inverttree(root, root2):
    if root:
        #print(root.val)
        root2 = Node(root.val)
        root2.left = inverttree(root.right, root2.left)
        root2.right = inverttree(root.left, root2.right)
    return root

'''
structure:
            8
        5       67
      3   7   15  99
    0  
'''

arr = [0, 5, 15, 67, 99, 3, 7, 8]
root1 = createbst(arr)
printtree(root1)
print("\n")
root2 = Node(root1.val)
inverttree(root1, root2)
printtree(root2)

