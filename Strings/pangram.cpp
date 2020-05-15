bool checkPangram (string &str)
{
    map<int,int> s;
    for(int i=0;i<str.length();i++){
        if(str[i]>='A' && str[i]<='Z'){
            str[i]+=32;
        }
        if(str[i]>='a' && str[i]<='z'){
            s[str[i]]++;
        }
    }
    if(s.size()==26){
        return(1);
    }
    return(0);
}