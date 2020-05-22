bool ispar(string str)
{
    stack<char> s;
    for(int i=0;i<str.length();i++){
        if(s.size()==0){
            s.push(str[i]);
        }
        else if((s.top()=='(' and str[i]==')') || (s.top()=='{' and str[i]=='}') 
        || (s.top()=='[' and str[i]==']')){
            s.pop();
        }
        else{
            s.push(str[i]);
        }
    }
    return(s.size()==0);
}