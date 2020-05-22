string removePair(string str){
    stack<char> s;
    string res = "";
    for(int i =0;i<str.length();i++){
        if(s.size()==0){
            s.push(str[i]);
            // cout<<s.top()<<" 1"<<endl;
        }
        else if(s.top()==str[i]){
            // cout<<str[i]<<" 2"<<endl;
            s.pop();
        }
        else{
            s.push(str[i]);
            // cout<<s.top()<<" 3"<<endl;
        }
    }
    // cout<<s.size()<<endl;
    while(s.size()!=0){
        res+=s.top();
        s.pop();
    }
    reverse(res.begin(),res.end());
    return(res);