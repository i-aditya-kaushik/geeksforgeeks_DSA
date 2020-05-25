void StackQueue :: push(int x)
 {
    s1.push(x);
 }

/*The method pop which return the element poped out of the queue*/
int StackQueue :: pop()
{   
    int n=s1.size();
    if(n==0){
        return(-1);
    }
    for(int i=0;i<n;i++){
        s2.push(s1.top());
        s1.pop();
    }
    int x = s2.top();
    s2.pop();
    for(int i=0;i<n-1;i++){
        s1.push(s2.top());
        s2.pop();
    }
    return(x);
}