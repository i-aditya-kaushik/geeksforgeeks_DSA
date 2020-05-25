void enqueue(queue<int> &s,int x)
{
   s.push(x);
}
 // Function to remove front element from queue
void dequeue(queue<int> &s)
{
    s.pop();
}
 // Function to find the front element of queue
void front(queue<int> &s)
{
    int x= s.front();
    cout<<x<<" "<<endl; 
}
 // Function to find the element in queue
void find(queue<int> s, int val)
{
    bool exists=false;
    while(s.size()!=0){
        if(s.front()==val){
            exists = true;
            break;
        }
        s.pop();
    }
    
    if(exists==true){
        cout<<"Yes"<<endl;
    }
    else{
        cout<<"No"<<endl;
    }
}