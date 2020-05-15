int modified (string a){
    map<int,int> s;
    int ans=0;
    for(int i=0;i<a.length();i++){
        s[a[i]]+=1;
        if(s.size()>=2){
            s.clear();
            s[a[i]]+=1;
        }
        if(s[a[i]]==3){
            ans+=1;
        }
        if(s[a[i]]>3){
            if(s[a[i]]%2==1)
                ans+=1;
        }
        // for(auto it=s.begin();it!=s.end();it++){
        //     cout<<it->first<<" "<<it->second<<endl;
        // }
    }
    return(ans);
}