def isIdentical(root1, root2):
    if(root1==None and root2!=None):
        return(0)
    if(root2==None and root1!=None):
        return(0)
    if(root1==None and root2==None):
        return(1)
    if(root1.data != root2.data):
        return(0)
    if(root1.left!=None and root2.left!=None):
        if(root1.left.data!=root2.left.data):
            return(0)
    if(root1.right!=None and root2.right!=None):
        if(root1.right.data!=root2.right.data):
            return(0)
    m = isIdentical(root1.left,root2.left)
    n = isIdentical(root1.right,root2.right)
    return(m&n)