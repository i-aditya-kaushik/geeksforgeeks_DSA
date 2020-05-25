void MyQueue :: push(int x)
{
    if (10001 == rear) { 
        return; 
    } 
    else{ 
        arr[rear] = x; 
        rear++; 
    } 
    return; 
}

/*The method pop which return the element 
  poped out of the queue*/
int MyQueue :: pop()
{
    int d;
    if (front == rear) { 
        return -1; 
    } 
    else { 
        d=arr[front];
        for (int i = 0; i < rear - 1; i++){ 
            arr[i] = arr[i + 1]; 
        } 
        rear--; 
    } 
    return d; 
}