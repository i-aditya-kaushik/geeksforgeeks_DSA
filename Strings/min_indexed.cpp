void printMinIndexChar(string str, string patt)
{
    map<int,int> s;
    for(int i=0;i<patt.length();i++){
        s[patt[i]]++;
    }
    for(int i=0;i<str.length();i++){
        if(s.find(str[i])!=s.end()){
            cout<<str[i];
            return;
        }
    }
    cout<<"No character present";
}