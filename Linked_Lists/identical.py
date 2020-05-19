def areIdentical(head1, head2):
    temp1= head1
    temp2 = head2
    while(temp1!=None and temp2!=None):
        if temp1.data!=temp2.data:
            return 0
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1!=None or temp2!=None:
        return 0
    return 1