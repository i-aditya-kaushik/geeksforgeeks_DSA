def removeDuplicates(head):
    l=[]
    while head:
        if head.data not in l:
            l.append(head.data)
        head=head.next
    b=LinkedList()
    for i in l:
        b.append(i)
    return b.head