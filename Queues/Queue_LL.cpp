void MyQueue:: push(int x)
{
        if(front==NULL){

        rear=new QueueNode(x);
        front=rear;
        return;
    }

    rear->next = new QueueNode(x);
    rear=rear->next;

}

/*The method pop which return the element
  poped out of the queue*/
int MyQueue :: pop()
{
    if (front==NULL)
        return -1;
    int a=front->data;
    front=front->next;
    return a;      
}