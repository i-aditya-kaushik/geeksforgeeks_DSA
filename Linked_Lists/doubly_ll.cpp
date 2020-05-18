void addNode(Node *head, int pos, int data)
{
    struct Node *temp ,*ptr ;
   
    temp=(struct Node*)malloc(sizeof(struct Node*)) ;
    temp->data=data ;
    temp->next=NULL ;
    temp->prev=NULL ;
    if(head==NULL){
        temp = head;
        return;
    }
    if(pos==0)
    {
        temp->next=(head)->next ;
        if((head)!= NULL)
            (head)->next=temp ;
            temp->prev = head;
        return;
    }
   
    ptr=(head);
    while(pos!=0)
    {
        ptr=ptr->next ;
        pos=pos-1 ;
    }
   
    temp->next=ptr->next ;
    if(ptr->next)
        ptr->next->prev=temp ;
    temp->prev=ptr ;
    ptr->next=temp ;
}