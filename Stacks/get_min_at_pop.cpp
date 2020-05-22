void _getMinAtPop(stack<int>s)
{
    list<int> t;
    while(s.size()!=0){
        if(t.size()==0){
            t.push_front(s.top());
            s.pop();
            continue;
        }
        if(*(t.begin())>s.top()){
            t.push_front(s.top());
            s.pop();
        }
        else{
            t.push_front(*(t.begin()));
            s.pop();
        }
    }
    for(int x:t){
        cout<<x<<" ";
    }
}