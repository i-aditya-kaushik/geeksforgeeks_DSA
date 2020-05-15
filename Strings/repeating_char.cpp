int repeatedCharacter (string str) 
{ 
    map <int,int> s;
    for(int i=0;i<str.length();i++){
        s[str[i]]++;
    }
    for(int i=0;i<str.length();i++){
        if(s[str[i]]>1){
            return i;
        }
    }
    return(-1);
} 