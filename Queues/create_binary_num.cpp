vector<string> generate(ll n)
{
    vector<string> v;
    v.push_back("1");
    int flag=0;
    for(int i=1;i<n/2 + 1;i++){ 
        v.push_back(v[i-1]+to_string(flag));
        if(v.size()==n){
            return(v);
        }
        v.push_back(v[i-1]+to_string(flag+1));
    }
    return(v);
}