def io(root,s):
    if root!=None:
        s= io(root.left,s)
        s.append(root.data)
        s = io(root.right,s)
    return(s)
# Return a list containing the inorder traversal of the given tree
def InOrder(root):
    s=[]
    return(io(root,s))
