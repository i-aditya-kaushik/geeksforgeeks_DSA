def insertInMid(head,node):
    fast,slow = head,head
    while(fast.next!=None and fast!=None):
        if(fast.next.next==None):
            break
        fast = fast.next.next
        slow = slow.next
    temp = node
    temp.next = slow.next
    slow.next = temp