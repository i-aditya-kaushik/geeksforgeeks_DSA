void winner(string arr[],int n)
{
    int max = -1;
    int index;
    map<string,int> s;
    for(int i=0;i<n;i++){
        s[arr[i]]+=1;
        if(s[arr[i]]>max){
            max=s[arr[i]];
        }
    }
    for(auto it=s.begin();it!=s.end();it++){
        if(it->second==max){
            cout<<it->first<<" "<<it->second;
            break;
        }
    }
}