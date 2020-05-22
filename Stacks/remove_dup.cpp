string removeConsecutiveDuplicates(string s)
{
    stack<int> s1;
    string res = "";
    for(int i=0;i<s.length();i++){
        if(s1.size()==0){
            s1.push(s[i]);
            res+=s[i];
            continue;
        }
        if(s1.top()==s[i]){
            continue;
        }
        s1.push(s[i]);
        res+=s[i];
    }
    return(res);
}