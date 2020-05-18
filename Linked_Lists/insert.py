def insertAtBegining(a,value):
    temp = Node(value)
    if(a.head==None):
        a.head = temp
        a.Tail=temp
        return a.head
    temp.next = a.head
    a.head = temp
    return a.head
    
# function should insert new node at the
# end of the list
def insertAtEnd(a,value):
    temp = Node(value)
    if(a.head==None):
        a.head=temp
        a.Tail=temp
        return a.head
    a.Tail.next = temp    
    a.Tail = temp
    return a.head