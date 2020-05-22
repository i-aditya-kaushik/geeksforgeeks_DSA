void insert(stack<int> &s,int x)
{
    s.push(x);
}

void remove(stack<int> &s)
{
    
    s.pop();
}

void headOf_Stack(stack<int> &s)
{
    int x= s.top();
    cout<<x<<" "<<endl; 
}

bool find(stack<int> s, int val)
{
    bool exists=false;
    
    stack<int> copy = s;
    
    while(copy.size()!=0){
        if(copy.top()==val){
            return(1);
        }
        copy.pop();
    }
    
    if(exists==true){
        return true;
    }
    else{
        return false;
    }
}