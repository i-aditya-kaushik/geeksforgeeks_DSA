def getCount(head_node):
    temp = head_node
    count=0
    while temp!=None:
        temp = temp.next
        count+=1
    return count