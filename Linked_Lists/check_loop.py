temp = head
    fast = head
    while(temp!=None and fast.next!=None and fast.next.next!=None):
        temp = temp.next
        fast = fast.next.next
        if temp==fast:
            return('True')
    return('False')