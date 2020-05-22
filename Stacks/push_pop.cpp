void MyStack :: push(int x)
{
    if(top==1000) return;
    arr[++top]=x;
}

/*The method pop which return the element 
  poped out of the stack*/
int MyStack :: pop()
{
    if(top==-1) return -1;
    return arr[top--];
}