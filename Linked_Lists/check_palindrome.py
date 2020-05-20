def isPalindrome(head):
    l1,l2 = [],[]
    temp = head
    while(temp!=None):
        l1.append(temp.data)
        l2.insert(0,temp.data)
        temp = temp.next
    return(l1 == l2)